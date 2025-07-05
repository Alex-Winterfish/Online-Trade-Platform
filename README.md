# Online-Trade-Platform
Онлайн платформа торговой сети электроники

## Установка проекта

Установить зависимости:
```commandline
pip install -r requerements.txt
```
Необходимые переменные окружения указны в файле .env.sample

Применить миграции:
```commandline
python manage.py migrate
```

Запустить сервер локально:
```commandline
python manage.py runserver
```

## Описание проекта

1. Использованные технологии:
- Проект написан на Python 3.13
- API реализован на Django Rest Framework 3.15.2
- В качестве базы данных использован PostgreSQL 10
- Документирование реализованно с помощью Swagger 1.21.10 http://127.0.0.1:8000/swagger/ или http://127.0.0.1:8000/redoc/


2. Структура проекта:
```
Online-Trade-Platform/
|
├───trade_net
│   ├───migrations
│   ├───tests
|   |   ├──__init__.py
|   |   ├──test_validators.py
|   |   └──test_view.py
|   ├──__init__.py 
│   ├──urls.py
│   ├──permissions.py
|   ├──serializers.py
|   ├──validator.py
│   ├──views.py
|   ├──admin.py
|   ├──apps.py
|   └──models.py
|
├───config
|
├───users
│   ├───migrations
|   ├──__init__.py 
|   ├──admin.py 
|   ├──apps.py
|   ├──models.py
|   ├──tests.py
|   ├──urls.py
|   └──views.py
└───venv
```

3. Описание моделей:

Приложение trade_net.

Модель NetUnitNodel. Модель объекта сети. Имеет следующие поля:

- unit_type - тип элемента сети. Поле принимает значения: "Завод", "ИП", "Торговая сеть". Тип CharField.
- name - название объекта. Тип CharField, максимальная длинна 150 символов
- email - электронная почта. Тип EmailField.
- country - страна. Тип CharField, максимальная длинна 100 символов
- city - город. Тип CharField, максимальная длинна 100 символов
- address - адрес объекта. Тип CharField, максимальная длинна 300 символов
- is_supplier - булево поле, по умолчанию False. Определяет, является ли объект сети поставщиком. Тип BooleanField. В случае, если поле unit_type="Завод" при создании объекта устанавливается True.
- supplier - внешний ключ на объект NetUnitModel, который является поставщиком (is_supplier=True)
- dept - задолженность перед поставщиком. Тип FloatField, по умолчанию 0.0
- created_at - время создания. Устанавливает текущие дату и время при создании объекта. Тип DateTimeField. 
- level - уровень элемента сети. Заполняется при создании объекта. Тип CharField, принимает значения Уровень 0, Уровень 1 или Уровень 2

Модель ProductModel. Модель объекта продукта. Имеет следующие поля:

- name - название продукта. Тип CharField, максимальная длинна 200 символов.
- model - модель продукта. Тип CharField, максимальна длинна 200 символов.
- release_date - дата выхода продукта на рынок. Тип DateField.

Приложение users

Модель CustomUser. Модель пользователя. Имеет следующие поля:

- username - псевдоним пользователя.
- email - электронная почта. Тип EmailField.
- phone - телефон пользователя. Тип CharField, максимальная длинна 35 символов.
- country - страна. Тип CharField, максимальная длинна 50 символов.

4. Отношения между моделями.

При создании объекта NetUnitModel в зависимости от его типа (unit_type) и отношения к поставщику, объект будет отнесен в один из 3 уровней (поле модели level):

- Уровень 0 - если объект представляет завод изготовитель
- Уровень 1 - если объект представляет ИП или точку торговой сети, которые являются поставщиками (поле модели is_supplier=True)
- Уровень 2 - если объект представляет ИП или точку торговой сети, которые не являются поставщиками (поле модели is_supplier=False)

При создании объекта ProductModel внешний ключ (поле модели manufacture) указывается на объект NetUnitModel, который является заводом изготовителем. В противном случае не проходиться валидация.

4. Валидация данных.

Для модели ProductModel.

- IsManufactureValidator - валидация установки внешнего ключа на завод-производитель

Для модели NetUnitModel.

- IsSupplierValidator - валидация установки внешнего ключа на модель поставщика
- NameValidator - валидация объекта сети "Завод" на совпадение имен существующих заводов в базе данных. Для объекта "Торговая сеть" проверяет совпадение адресов.
- AddressValidator - валидация адреса.

## Использование приложения
1. Регистрация пользователя.
Доступ к приложению имеют авторизированные пользователи в статусе сотрудников. Эндпоинт для регистрации пользователя:

http://127.0.0.1:8000/register/

Пример POST запроса:

{
    "username": "Olga",
    "email": "user_6@mail.com",
    "country": "Russia",
    "password": 12345
}

При регистрации пользователя поле is_staff устанавливается True

Аутентификация пользователя осуществляется адресу электронной почты и паролю. Эндпоинт http://127.0.0.1:8000/login/

Пример POST запроса:

{
    "email": "user_6@mail.com",
    "password": 12345
}

2. Эндпоинты.

http://127.0.0.1:8000/net-unit-create/ - создание объекта сети
http://127.0.0.1:8000/net-unit-retrieve/<int:pk>/ - получение объекта сети
http://127.0.0.1:8000/net-unit-update/<int:pk>/ - изменение объекта сети
http://127.0.0.1:8000/net-unit-destroy/<int:pk>/ - удаление объекта сети
http://127.0.0.1:8000/net-unit-list/ - получение списка объектов сети
http://127.0.0.1:8000/product-create/ - создание продукта
http://127.0.0.1:8000/product-retrieve/<int:pk>/ - получение продукта
http://127.0.0.1:8000/product-update/<int:pk>/ - изменение продукта
http://127.0.0.1:8000/product-destroy/<int:pk>/ - удаление продукта
http://127.0.0.1:8000/product-list/ - получение списка продуктов

3. Сериализация.

В проекте настроена пагинация. Выводится по 100 объектов.
Пример вывода списка объектов NetUnitModel:

{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "unit_type": "Завод",
            "name": "Завод Огр Техники",
            "email": "manuf_2@mail.com",
            "country": "Россия",
            "city": "Москва",
            "address": "Космонавтов 11",
            "is_supplier": true,
            "supplier": null,
            "dept": 0.0,
            "produced_prod": [
                {
                    "name": "Принтер",
                    "model": "Python N3",
                    "release_date": "2025-06-28",
                    "manufacture": 2
                }
            ],
            "retail_prod": [],
            "created_at": "2025-06-28T11:45:00.299000Z"
        },
        {
            "id": 7,
            "unit_type": "Завод",
            "name": "Тестовый Завод Посуды",
            "email": "manuf_3@mail.com",
            "country": "Россия",
            "city": "Москва",
            "address": "ул. Космонавтов, д. 12",
            "is_supplier": true,
            "supplier": null,
            "dept": 0.0,
            "produced_prod": [],
            "retail_prod": [],
            "created_at": "2025-07-05T11:05:23.447939Z"
        },
        {
            "id": 1,
            "unit_type": "Завод",
            "name": "Завод бытовой техники",
            "email": "manuf_1@gmail.com",
            "country": "Китай",
            "city": "Пекин",
            "address": "ул. Ленина д.2",
            "is_supplier": true,
            "supplier": null,
            "dept": 0.0,
            "produced_prod": [
                {
                    "name": "Стиральная машина",
                    "model": "Candy M-2",
                    "release_date": "2025-06-10",
                    "manufacture": 1
                }
            ],
            "retail_prod": [],
            "created_at": "2025-06-28T11:44:05.212000Z"
        }
    ]
}

Пример вывода объекта NetUnitModel уровня 0 (завод):

{
            "id": 1,
            "unit_type": "Завод",
            "name": "Завод бытовой техники",
            "email": "manuf_1@gmail.com",
            "country": "Китай",
            "city": "Пекин",
            "address": "ул. Ленина д.2",
            "is_supplier": true,
            "supplier": null,
            "dept": 0.0,
            "produced_prod": [
                {
                    "name": "Стиральная машина",
                    "model": "Candy M-2",
                    "release_date": "2025-06-10",
                    "manufacture": 1
                }
            ],
            "retail_prod": [],
            "created_at": "2025-06-28T11:44:05.212000Z"
        }
produced_prod - список объектов ProductModel у которых внешний ключ установлен на текущий объект NetUnitModel ()

Пример вывода объекта NetUnitModel уровня 1 (поставщик, ИП или Торговая сеть ):

{
    "id": 3,
    "unit_type": "Торговая сеть",
    "name": "Эльдорадо",
    "email": "eldorado@mai.com",
    "country": "Россия",
    "city": "Пермь",
    "address": "ул. Джержинского д.2",
    "is_supplier": true,
    "supplier": 1,
    "dept": 0.0,
    "produced_prod": [],
    "retail_prod": [
        {
            "name": "Стиральная машина",
            "model": "Candy M-2",
            "release_date": "2025-06-10",
            "manufacture": 1
        }
    ],
    "created_at": "2025-06-28T11:57:52.005000Z"
}

retail_prod - список объектов ProductModel от связанного объекта завода-производителя.

Пример вывода объекта NetUnitModel уровня 2 (продовец, ИП или Торговая сеть ):

{
    "id": 4,
    "unit_type": "ИП",
    "name": "ИП Малахов",
    "email": "ep_malahov@mail.com",
    "country": "Россия",
    "city": "Старый Оскол",
    "address": "мкр Степной д.1",
    "is_supplier": false,
    "supplier": 3,
    "dept": 0.0,
    "produced_prod": [],
    "retail_prod": [
        {
            "name": "Стиральная машина",
            "model": "Candy M-2",
            "release_date": "2025-06-10",
            "manufacture": 1
        }
    ],
    "created_at": "2025-06-28T12:00:02.664000Z"
}

retail_prod - список объектов ProductModel от связанного объекта поставщика.

Пример вывода объекта ProductModel:

{
    "name": "Стиральная машина",
    "model": "Candy M-2",
    "release_date": "2025-06-10",
    "manufacture": 1
}

4. Фильтры.

Настроена фильтрация для списка объектов сети по типу объекта(unit_type), городу(city), стране(country) уровню в иерархии(level)

Пример POST запроса:

http://127.0.0.1:8000/net-unit-list?country=Россия&city=Москва&level=Уровень 2

5. Админ-панель.

В админ панели реализованно admin-action "Очистить задолженность", которое устанавливает значение 0.0 в поле dept модели NetUnitMode. Изменение поля dept через API запрещено в сериализаторе.

Настроена фильтрация по типу элемента сети "Собственник", Названию, Стране, Городу и уровню элемента в сети.

6. Тестировние.

проект покрыт тестами на 91%

запустить тестирование:
```commandline
coverage run manage.py test
```
Name                                   Stmts   Miss  Cover
----------------------------------------------------------
__init__.py                                0      0   100%
config\__init__.py                         0      0   100%
config\settings.py                        25      0   100%
config\urls.py                             7      0   100%
manage.py                                 11      2    82%
trade_net\__init__.py                      0      0   100%
trade_net\admin.py                        25      5    80%
trade_net\apps.py                          4      0   100%
trade_net\migrations\0001_initial.py       6      0   100%
trade_net\migrations\__init__.py           0      0   100%
trade_net\models.py                       40      6    85%
trade_net\permissions.py                   6      0   100%
trade_net\serializers.py                  30     10    67%
trade_net\tests\__init__.py                0      0   100%
trade_net\tests\test_validators.py        38      0   100%
trade_net\tests\test_view.py              52      0   100%
trade_net\urls.py                          5      0   100%
trade_net\validators.py                   46      0   100%
trade_net\views.py                        52      3    94%
users\__init__.py                          0      0   100%
users\admin.py                             5      0   100%
users\apps.py                              4      0   100%
users\migrations\0001_initial.py           8      0   100%
users\migrations\__init__.py               0      0   100%
users\models.py                           15      1    93%
users\serializers.py                       6      0   100%
users\tests.py                             1      0   100%
users\urls.py                             11      0   100%
users\views.py                            32     10    69%
----------------------------------------------------------
TOTAL                                    429     37    91%

Отчет о покрытии тестами сохранен в html






