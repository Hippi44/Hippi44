"""Build a small profile card from public GitHub data, without third-party APIs.

The account creation year is not a claim about professional experience.
Forks and archived repositories count as public repositories. TypeScript means
the repository's primary language reported by GitHub, not a skill score.
An unchanged snapshot keeps its date, so scheduled runs do not create empty
or date-only commits. API failures leave the last successful snapshot intact.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os
from pathlib import Path
import re
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
API = "https://api.github.com"
THEMES = {
    "light": {
        "background": "#F6F8FA",
        "border": "#D8DEE4",
        "text": "#1F2328",
        "muted": "#57606A",
        "accent": "#446B34",
    },
    "dark": {
        "background": "#161B22",
        "border": "#30363D",
        "text": "#F0F3F6",
        "muted": "#9DA7B3",
        "accent": "#B7D79C",
    },
}


def github_json(path: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "github-profile-public-metrics",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"{API}{path}", headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def collect_metrics(username: str) -> dict:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", username):
        raise ValueError("Invalid GitHub username")

    profile = github_json(f"/users/{username}")
    if profile["login"].lower() != username.lower():
        raise ValueError("GitHub returned a different user")

    repositories = []
    page = 1
    while True:
        batch = github_json(
            f"/users/{username}/repos?type=owner&per_page=100&page={page}"
        )
        if not isinstance(batch, list):
            raise ValueError("Expected a public repository list")
        repositories.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    public = [
        repo
        for repo in repositories
        if repo.get("private") is False
        and repo.get("visibility", "public") == "public"
        and repo["owner"]["login"].lower() == username.lower()
    ]

    return {
        "username": profile["login"],
        "public_repositories": len(public),
        "typescript_repositories": sum(
            repo.get("language") == "TypeScript" for repo in public
        ),
        "account_created_at": profile["created_at"],
        "source": {
            "profile": f"{API}/users/{username}",
            "repositories": (
                f"{API}/users/{username}/repos?type=owner&per_page=100"
            ),
            "scope": "Public owned repositories, including forks and archives",
            "typescript_definition": "repository.language == TypeScript",
        },
    }


def make_snapshot(
    metrics: dict, previous: dict | None = None, as_of: str | None = None
) -> dict:
    if previous is not None:
        previous_data = {
            key: value for key, value in previous.items() if key != "updated_at"
        }
        if previous_data == metrics and "updated_at" in previous:
            return previous
    date = as_of or dt.datetime.now(dt.timezone.utc).date().isoformat()
    return {**metrics, "updated_at": date}


def render_svg(snapshot: dict, theme: str) -> str:
    colors = THEMES[theme]
    for key in ("public_repositories", "typescript_repositories"):
        value = snapshot[key]
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"Invalid metric: {key}")
    if snapshot["typescript_repositories"] > snapshot["public_repositories"]:
        raise ValueError("Language count exceeds public repository count")

    year = dt.datetime.fromisoformat(
        snapshot["account_created_at"].replace("Z", "+00:00")
    ).year
    date = dt.date.fromisoformat(snapshot["updated_at"]).strftime("%d.%m.%Y")
    username = html.escape(snapshot["username"])
    public = snapshot["public_repositories"]
    typescript = snapshot["typescript_repositories"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="188" viewBox="0 0 1200 188" role="img" aria-labelledby="title desc">
  <title id="title">Публичная статистика GitHub · {username}</title>
  <desc id="desc">{public} публичных репозиториев; {typescript} репозиториев с основным языком TypeScript; аккаунт создан в {year} году. Снимок данных: {date}. Год создания аккаунта не означает стаж работы.</desc>
  <rect x="1" y="1" width="1198" height="186" rx="18" fill="{colors['background']}" stroke="{colors['border']}"/>
  <path d="M 400 32 V 123 M 800 32 V 123" stroke="{colors['border']}"/>
  <g font-family="Segoe UI, Arial, sans-serif">
    <g fill="{colors['accent']}" font-size="52" font-weight="700" letter-spacing="-1">
      <text x="44" y="85">{public}</text>
      <text x="444" y="85">{typescript}</text>
      <text x="844" y="85">{year}</text>
    </g>
    <g fill="{colors['text']}" font-size="20" font-weight="500">
      <text x="44" y="119">публичных репозиториев</text>
      <text x="444" y="119">TypeScript-репозиториев</text>
      <text x="844" y="119">аккаунт на GitHub с</text>
    </g>
    <text x="44" y="163" fill="{colors['muted']}" font-size="17">GitHub API · публичные данные · обновлено {date}</text>
  </g>
</svg>
'''


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def main() -> None:
    username = os.environ.get("GITHUB_USERNAME", "Hippi44")
    assets = ROOT / "assets"
    data_path = assets / "github-metrics.json"
    previous = (
        json.loads(data_path.read_text(encoding="utf-8"))
        if data_path.exists()
        else None
    )
    snapshot = make_snapshot(collect_metrics(username), previous)

    # Fetch and validate everything before changing any saved output.
    outputs = {
        data_path: json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n",
        assets / "github-metrics-light.svg": render_svg(snapshot, "light"),
        assets / "github-metrics-dark.svg": render_svg(snapshot, "dark"),
    }
    assets.mkdir(parents=True, exist_ok=True)
    changed = [
        path.name
        for path, content in outputs.items()
        if write_if_changed(path, content)
    ]
    print(
        f"{snapshot['username']}: {snapshot['public_repositories']} public repos, "
        f"{snapshot['typescript_repositories']} primarily TypeScript"
    )
    print("Updated: " + ", ".join(changed) if changed else "Metrics unchanged")


if __name__ == "__main__":
    main()
