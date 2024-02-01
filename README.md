# Тестирование веб-приложения (Диплом.Часть 3).

Автотесты для веб-приложения Stellar Burgers (https://stellarburgers.nomoreparties.site/).

## Установка

1. Склонируйте репозиторий на локальную машину:

git clone https://github.com/your_username/your_project.git

2. Перейдите в каталог проекта:

cd your_project

3. Создайте виртуальное окружение и активируйте его:

python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Linux/Mac)

4. Установите зависимости:

pip install -r requirements.txt

## Запуск тестов

1. Перейдите в каталог с тестами:

cd tests

2. Запустите тесты с помощью pytest:

pytest

Тесты так же можно запускать с помощь файла start.bat

## Структура проекта

- endpoints/ - модули с API-запросами
- locators/ - локаторы элементов на страницах
- pages/ - объекты страниц и действия на них
- services/ - вспомогательные модули для генерации данных и запросов
- tests/ - тесты на функционал
