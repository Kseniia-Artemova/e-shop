# e-shop

Как загрузить данные в БД для корректного отображения сайта:
1. Установить зависимости в venv (pip install -r requirements.txt)
2. В файл e-shop/.env внести данные о своей базе данных, куда следует сохранять данные
3. Ввести команду python manage.py loaddata data.json
4. Запустить сайт (python manage.py runserver)