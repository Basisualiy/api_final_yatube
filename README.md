# Yatube_Api
Api для сервиса написания постов, поддерживает комментарии и подписки на других пользователей.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Тестирование](#тестирование)



## Технологии
- [Django](https://www.djangoproject.com/)
- [Django Rest framework](https://www.django-rest-framework.org/)
- ...

## Разработка

### Требования
Для установки и запуска проекта, необходимо склонировать проект с [GitHub](https://github.com/Basisualiy/api_final_yatube).
Перейти в папку проекта:
```sh
cd api_final_yatube
```
Создать виртуальное окружение:
```sh
python -m venv .venv
```

Активировать его:
(Windows)
```sh
.venv/Scripts/Activate
```
(Linux)
```sh
source .venv/bin/activate
```

### Установка зависимостей
Для установки зависимостей, выполните команду:
```sh
pip install -r requirements.txt
```
Применение миграций:
```sh
python yatube_api/manage.py migrate
```
Создание суперпользователя:
```sh
python yatube_api/manage.py createsuperuser
```

### Запуск Development сервера
Чтобы запустить сервер для разработки, выполните команду:
```sh
python yatube_api/manage.py runserver
```


## Тестирование

Наш проект покрыт тестами PyTest. Для их запуска выполните команду:
```sh
pytest
```

### Зачем вы разработали этот проект?
Данный проект разработан в рамках обучения на платформе [Yandex Practicum](https://practicum.yandex.ru/).

Ссылка на промокод [Python-разработчик расширенный. Скидка 7%](https://practicum.yandex.ru/referrals/?ref_code=gAAAAABmsb81icFtgbTyIna3zTQylZcMLMCu2I2GpDjFqivakjt__Vf8EsXx8VAgNUkmatzBLNe_6Z9eWsE-jzOjIS4FdN1PdQ%3D%3D)