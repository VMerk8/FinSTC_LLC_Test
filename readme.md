ТЕСТОВОЕ ЗАДАНИЕ на позицию Разработчик Python

Задание:
1. Создать небольшое REST API на Python (можно использовать любые библиотеки и framework-и, в т.ч. Flask).
2. Требуется создание только бэкэнд части, в readme файле желательно описать endpoint и примеры запросов (будет плюсом наличие файлов-схем запросов, например JSON Schema).
3. Данное API должно поддерживать CRUD операции.
4. Тематика данного API связана с продажами машин автодилерами. Модель данных (в т.ч. описание и взаимодействие между классами "Машина" и "Дилер") можете разработать любую, на ваше усмотрение, но соответствующую условиям выше.

Для запуска проекта необходимо проинсталировать requirements.
Далее необходимо сделать миграции командами "python3 manage.py makemigrations" и "python3 manage.py migrate"


Описание работы запросов.
Запускаем сервер;
Переходим по адресу http://127.0.0.1:8000/api/ (Если при запуске выбрали 8000 порт, если другой, то он будет отличаться). 

Примеры запросов:
http://127.0.0.1:8000/api/dealer/ - выдаёт список всех дилеров
http://127.0.0.1:8000/api/dealer/1 - выдаёт первого дилера
http://127.0.0.1:8000/api/car/ - выдаёт список всех автомобилей
http://127.0.0.1:8000/api/car/1 - выдаёт первый автомобиль
http://127.0.0.1:8000/api/manufacturer/ - выдаёт список всех производителей
http://127.0.0.1:8000/api/manufacturer/1 - выдаёт первого производителя

Delete, Put и Patch запросы работают с id на конце адреса, выбираем необходимый и изменяем необходимые поля, либо удаляем запись целиком.
Удобно проверять через Postman, но и с помощью встроенного интерфейса в DRF можно (все кнопки есть).

http://127.0.0.1:8000/api/car/get_manufacturer_cars/?manufacturer_id=1 - запрос выдаёт список автомобилей, которые есть у данного производителя.
http://127.0.0.1:8000/api/car/get_dealer_cars/?dealer_id=1 - запрос выдаёт список автомобилей, которые есть у данного дилера.
