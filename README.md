<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img src="assets/header-light.svg" alt="Hippilokkery — Fullstack Developer. Web, API, Telegram." width="100%">
</picture>

Разрабатываю **веб-интерфейсы, серверные API и Telegram-интеграции**.
В моих открытых проектах — React и TypeScript, Node.js, базы данных и автоматизация обработки заявок.

[![Telegram — @Hippilokkery](https://img.shields.io/badge/Telegram-%40Hippilokkery-1F2937?style=for-the-badge&logo=telegram&logoColor=B7D79C)](https://t.me/Hippilokkery) [![Веб-портфолио](https://img.shields.io/badge/Portfolio-Website-1F2937?style=for-the-badge&logo=githubpages&logoColor=B7D79C)](https://hippi44.github.io/portfolio/)

## Технологии

**Frontend**

![TypeScript](https://img.shields.io/badge/TypeScript-1F2937?style=flat&logo=typescript&logoColor=9EB8D0) ![JavaScript](https://img.shields.io/badge/JavaScript-1F2937?style=flat&logo=javascript&logoColor=D8CDA6) ![React](https://img.shields.io/badge/React-1F2937?style=flat&logo=react&logoColor=9EB8D0) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-1F2937?style=flat&logo=tailwindcss&logoColor=9EB8D0)

**Backend и данные**

![Node.js](https://img.shields.io/badge/Node.js-1F2937?style=flat&logo=nodedotjs&logoColor=B7D79C) ![NestJS](https://img.shields.io/badge/NestJS-1F2937?style=flat&logo=nestjs&logoColor=DBADB6) ![Express](https://img.shields.io/badge/Express-1F2937?style=flat&logo=express&logoColor=D1D5DB) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-1F2937?style=flat&logo=postgresql&logoColor=9EB8D0) ![MongoDB](https://img.shields.io/badge/MongoDB-1F2937?style=flat&logo=mongodb&logoColor=B7D79C) ![Redis](https://img.shields.io/badge/Redis-1F2937?style=flat&logo=redis&logoColor=DBADB6)

**Инструменты и тестирование**

![Docker](https://img.shields.io/badge/Docker-1F2937?style=flat&logo=docker&logoColor=9EB8D0) ![Jest](https://img.shields.io/badge/Jest-1F2937?style=flat&logo=jest&logoColor=DBADB6) ![Playwright](https://img.shields.io/badge/Playwright-1F2937?style=flat)

Prisma · BullMQ · Vite · GitHub Actions · HTML · CSS / SCSS

## Избранные проекты

### Automation System

**Обработка заявок через Telegram и событийные workflow.** Демонстрационный контур: бот → API → очередь → обработчик сценариев.
Заявки и журнал выполнения сохраняются в PostgreSQL; реализованы фоновые задачи, повторные попытки и защита от дублирования.

<sub>TypeScript · NestJS · PostgreSQL · Prisma · Redis · BullMQ · Docker</sub>

[Репозиторий](https://github.com/Hippi44/automation-system) · [Архитектура и запуск](https://github.com/Hippi44/automation-system/blob/main/README.md)

### Web-Larёk · Express API

**Учебный fullstack-проект интернет-магазина.** React-интерфейс и Express API: каталог в MongoDB, JWT-авторизация с обновлением токенов, защищённое управление товарами и загрузка изображений.
Состав и стоимость заказа проверяются на сервере.

<sub>React · TypeScript · Node.js · Express · MongoDB · Mongoose · JWT</sub>

[Репозиторий](https://github.com/Hippi44/web-larek-express) · [Реализация: `review-admin`](https://github.com/Hippi44/web-larek-express/tree/review-admin)

### Stellar Burgers

**Учебное React-приложение для сборки бургеров.** Состояние конструктора на Redux Toolkit, работа с внешним API, авторизация, защищённые маршруты и история заказов.
В репозитории есть unit-тесты редьюсеров на Jest и браузерные сценарии на Playwright с подменой API через HAR.

<sub>React · TypeScript · Redux Toolkit · React Router · Jest · Playwright</sub>

[Репозиторий](https://github.com/Hippi44/stellar-burgers) · [Реализация: `review`](https://github.com/Hippi44/stellar-burgers/tree/review) · [E2E-тесты](https://github.com/Hippi44/stellar-burgers/tree/review/tests)

### BoostPay

**Frontend-демо каталога цифровых товаров.** Поиск и фильтры, избранное, личный кабинет и административный интерфейс для управления каталогом и заказами.
Данные и демонстрационная авторизация работают через `localStorage`; серверная авторизация и реальные платежи не подключены.

<sub>React · TypeScript · React Router · Vite · CSS Modules</sub>

[Репозиторий](https://github.com/Hippi44/boostpay-app) · [Открыть демо](https://hippi44.github.io/boostpay-app/)

### NOKTURN

**Адаптивный лендинг детейлинг-студии без фреймворков.** Интерактивное сравнение «до/после» с управлением мышью, касанием и клавиатурой, галерея на `<dialog>`, фильтры и клиентская валидация формы.
Предусмотрены семантическая разметка и поддержка `prefers-reduced-motion`.

<sub>HTML · CSS · JavaScript · Pointer Events · Web Accessibility</sub>

[Репозиторий](https://github.com/Hippi44/lendingPage) · [Открыть сайт](https://hippi44.github.io/lendingPage/)

**Ещё один веб-проект:** [Electric Line](https://github.com/Hippi44/ElectricLine) — React-лендинг с Tailwind CSS, анимациями и карточками моделей. [Посмотреть сайт](https://hippi44.github.io/ElectricLine/).

## Мой продукт · Biba VPN

**[Biba VPN — @BibaVPN_bot](https://t.me/BibaVPN_bot)** — мой VPN-сервис с Telegram-ботом: подключение, тарифы и помощь прямо в Telegram.

[![Открыть Biba VPN в Telegram](https://img.shields.io/badge/Biba_VPN-Open_bot-1F2937?style=for-the-badge&logo=telegram&logoColor=B7D79C)](https://t.me/BibaVPN_bot)

По вопросам разработки и сотрудничества: **[@Hippilokkery](https://t.me/Hippilokkery)**.

## GitHub · публичный код

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/github-metrics-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/github-metrics-light.svg">
  <img src="assets/github-metrics-light.svg" alt="Статистика публичных репозиториев Hippi44: число репозиториев, репозитории с основным языком TypeScript и год создания аккаунта. Актуальные значения — в SVG и исходных данных по ссылке ниже." width="100%">
</picture>

<sub>Только публичные данные GitHub API. TypeScript учитывается как основной язык репозитория. Карточка обновляется еженедельно при изменении показателей. [Данные](https://github.com/Hippi44/Hippi44/blob/main/assets/github-metrics.json) · [История активности](https://github.com/Hippi44?tab=overview)</sub>

## Связаться

Обсудить веб-проект, Telegram-интеграцию или сотрудничество — **[@Hippilokkery](https://t.me/Hippilokkery)**.

[![Написать @Hippilokkery в Telegram](https://img.shields.io/badge/Telegram-%40Hippilokkery-1F2937?style=for-the-badge&logo=telegram&logoColor=B7D79C)](https://t.me/Hippilokkery)

[Веб-портфолио](https://hippi44.github.io/portfolio/) · [GitHub](https://github.com/Hippi44)
