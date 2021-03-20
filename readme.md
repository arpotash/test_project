Задание:
1. Создать небольшое REST API на Python (можно использовать любые библиотеки и framework-и, в т.ч. Flask).
2. Требуется создание только бэкэнд части, в readme файле желательно описать endpoint и примеры запросов (будет плюсом наличие файлов-схем запросов, например JSON Schema).
3. Данное API должно поддерживать CRUD операции.
4. Тематика данного API связана с продажами машин автодилерами. Модель данных (в т.ч. описание и взаимодействие между классами "Машина" и "Дилер") можете разработать любую, на ваше усмотрение, но соответствующую условиям выше.

Документация к api находится по адресу: http://127.0.0.1:8000/swagger/

endpoints:
1. http://127.0.0.1:8000/admin/ - стандартная админка
2. http://127.0.0.1:8000/api-auth/ - авторизация от drf
3. http://127.0.0.1:8000/api/cars/ - вывод списка автомобилей
4. http://127.0.0.1:8000/api/cars/create/ - создание автомобиля
5. http://127.0.0.1:8000/api/cars/detail/<int:pk>/ - просмотр информации об одном автомобиле, редактирование, удаление
6. http://127.0.0.1:8000/api/organizations/ - вывод списка организаций
7. http://127.0.0.1:8000/api/organizations/create - создание организации
8. http://127.0.0.1:8000/api/organizations/detail/<int:pk>/ - просмотр информации об одном автомобиле, редактирование, удаление


1. Для запуска приложения необходимо выполнить установку необходимых библиотек из файла requirements.txt
pip install -r requirements.txt
2. Сделать все миграции в базу данных:
python(python3 - для маков, линукса) manage.py migrate
3. Запустить сервер:
python(3) manage.py runserver
4. Для наполнения начальными данными нужно запустить команду:
python(3) manage.py load_from_file
5. Для создания суперпользователя:
python(3) manage.py createsuperuser
   
Пользовательские логи попадают в файл logfile.log
