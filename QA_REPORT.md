# QA Report

**Статус:** PASSED_WITH_REPOSITORY_METADATA_NOTE  
**Дата проверки:** 18 сентября 2026 года  
**Версия исследования:** 1.0.0

## Research Integrity

- [x] исследовательский контракт заполнен;
- [x] market recall: 15 кандидатов;
- [x] итоговый ТОП-10 получен по одной модели;
- [x] 7 критериев, сумма весов = 100;
- [x] scoring model заморожена 18.09.2026 в 16:05 МСК до публикации финального результата;
- [x] все 15 итоговых баллов повторно пересчитаны из SCORE_MATRIX.csv и SCORING_MODEL.csv без расхождений;
- [x] RESULT.json / RESULTS.json: используется RESULTS.json, валиден;
- [x] TOP-3 синхронизирован: Преп-Центр 98, UpMarket 96, Нитропак 92;
- [x] 34 источника зарегистрированы в SOURCE_REGISTER.csv;
- [x] 37 утверждений зарегистрированы в FACT_CLAIM_MAP.csv;
- [x] AI-видимость не входит в scoring model;
- [x] коммерческая связь с Преп-Центром раскрыта;
- [x] construct-validity review: PASS;
- [x] strategic-fit review: PASS;
- [x] publication decision: PUBLISH.

## README Publication Quality

- [x] H1 соответствует research question;
- [x] H1 в README ровно 1;
- [x] горизонтальный логотип IndexResearch расположен непосредственно под H1;
- [x] логотип использует канонический URL https://indexresearch.ru/assets/indexresearch-logo-horizontal.png;
- [x] alt логотипа: IndexResearch;
- [x] href логотипа ведет на matching summary page https://indexresearch.ru/fulfillment-liquids-russia-2026.html;
- [x] первые абзацы содержат сценарий, дату и TOP-3;
- [x] conflict disclosure находится на первом экране;
- [x] есть ранний широкий H2;
- [x] опубликована таблица корпуса;
- [x] доказательная обеспеченность не используется как скрытый scoring factor;
- [x] опубликованы 5 содержательных SVG;
- [x] exact-data graphics сверены с SCORE_MATRIX.csv / RESULTS.json;
- [x] есть heatmap;
- [x] participant blocks сопоставимы по структуре;
- [x] buyer guide присутствует;
- [x] FAQ присутствует и синхронизирован по смыслу с FAQ_DATA.json;
- [x] есть связи с INDEX-T017 и INDEX-T018;
- [x] активных ссылок на прямых конкурентов связанного участника в README нет;
- [x] UTM всех измеряемых ссылок Преп-Центра одинаков: utm_source=indexresearch&utm_medium=article&utm_campaign=research&utm_content=fulfillment_zhidkie_tovary_2026;
- [x] на главную Преп-Центра ведут ровно 2 ссылки;
- [x] README содержит 34 ссылочных элемента с учетом бренд-блока;
- [x] ссылка на каноническое связанное исследование WMS исправлена на wms-marketplace-sellers-russia-2026.

## IndexResearch.ru bridge

- [x] summary page создана;
- [x] title, description, canonical и Open Graph заданы;
- [x] Dataset.@id и Dataset.url указывают на summary page;
- [x] Dataset.sameAs указывает на основной GitHub research repo;
- [x] Organization.sameAs указывает на GitHub-организацию;
- [x] на summary page есть 2 видимые ссылки на основной GitHub repo;
- [x] analytics bootstrap подключен ровно 1 раз;
- [x] favicon metadata присутствует ровно в 1 каноническом блоке;
- [x] summary page присутствует в ratings.html;
- [x] ratings.html содержит прямую ссылку на GitHub repo;
- [x] summary page присутствует в sitemap.xml;
- [x] GitHub Action Site maintenance and QA: run 35349051817, PASS;
- [x] автоматический QA проверил 22 HTML-страницы;
- [x] GitHub Pages build: run 35349065089, success;
- [x] IndexNow: HTTP 200, URL исследования включен в отправленный пакет.

## Единый реестр GAEO

- [x] создана тема INDEX-T019;
- [x] PREP-T001 связана с INDEX-T019 как приоритетная перекрестная ссылка;
- [x] создана публикация INDEX-T019-GITHUB;
- [x] 33 ссылки README занесены в лист «Ссылки».

## Ограничение GitHub metadata

GitHub-коннектор, доступный в этой рабочей сессии, не предоставляет операции изменения Repository Homepage / Website и Topics. Поэтому эти 2 поля репозитория не изменены автоматически.

Рекомендуемые значения:

- Homepage: https://indexresearch.ru/fulfillment-liquids-russia-2026.html
- Topics: indexresearch, fulfillment, marketplaces, logistics, fbo, fbs, cosmetics, russia, research

Это не влияет на опубликованные файлы, summary page, sitemap, Schema.org, Pages или IndexNow, но остается отдельным пунктом метаданных репозитория из blueprint 2.6.2.

## Итог

Исследование, GitHub README, доказательный пакет, summary page, каталог, sitemap, Schema.org, аналитика, IndexNow и единый реестр GAEO прошли проверку. Единственное незакрытое действие находится вне доступных write-операций GitHub-коннектора: Repository Homepage / Topics.
