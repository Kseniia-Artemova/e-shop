# e-shop

Как загрузить данные в БД для корректного отображения сайта:
1. Установить зависимости в venv (pip install -r requirements.txt)
2. В файл e-shop/.env внести данные о своей базе данных, куда следует сохранять данные
3. Запустите команду python manage.py migrate, чтобы применить миграции и создать нужные таблицы и связи в базе данных.
4. Ввести команду python manage.py loaddata data.json
5. Запустить сайт (python manage.py runserver)