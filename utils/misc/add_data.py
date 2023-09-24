import psycopg2
from data import config

categories = [
    {
        "name": "🎧 Электроника" #1
    },
    {
        "name": "🔌 Бытовая техника" #2
    },
    {
        "name": "👕 Одежда" #3
    },
    {
        "name": "👟 Обувь" #4
    },
    {
        "name": "🎒 Аксессуары" #5
    },
    {
        "name": "💄 Красота" #6
    },
    {
        "name": "❤️ Здоровье" #7
    },
    {
        "name": "🏠 Товары для дома" #8
    },
    {
        "name": "🧱 Строительство и ремонт" #9
    },
    {
        "name": "🚘 Автотовары" #10
    },
    {
        "name": "🧸 Детские товары" #11
    },
    {
        "name": "🎨 Хобби и творчество" #12
    },
    {
        "name": "🏀 Спорт и отдых" #13
    },
    {
        "name": "🍏 Продукты и питания" #14
    },
    {
        "name": "🧴 Бытовая химия и личная гигиена" #15
    },
    {
        "name": "📔 Канцтоварые" #16
    },
    {
        "name": "🐾 Зоотовары" #17
    },
    {
        "name": "📖 Книги" #18
    },
    {
        "name": "🍃 Дачаб сад и огород" #19
    },
    {
        "name": "Смартфоны и телефоны", #20
        "parent_id": 1
    },
    {
        "name": "Умные часы и фитнес браслеты", #21
        "parent_id": 1
    },
    {
        "name": "Ноутбуки, планшеты и электронные книги", #22
        "parent_id": 1
    },
    {
        "name": "Комьютерная техника", #23
        "parent_id": 1
    },
    {
        "name": "Наушники и аудиотехники", #24
        "parent_id": 1
    },
    {
        "name": "Фото и фидеотехника", #25
        "parent_id": 1
    },
    {
        "name": "Часы и электронные будильники", #26
        "parent_id": 1
    },
    {
        "name": "Умный дом и безопасность", #27
        "parent_id": 1
    },
    {
        "name": "Телевизоры и видеотехника", #28
        "parent_id": 1
    },
    {
        "name": "Квадрокоптеры и аксессуары", #29
        "parent_id": 1
    },
    {
        "name": "Игровые приставки", #30
        "parent_id": 1
    },
    {
        "name": "Навигаторы", #31
        "parent_id": 1
    },
    {
        "name": "Офисная техника", #32
        "parent_id": 1
    },
    {
        "name": "Оптические приборы", #33
        "parent_id": 1
    },
    {
        "name": "Аксессуары для электроники", #34
        "parent_id": 1
    },
    {
        "name": "Смартфоны и телефоны", #20
        "parent_id": 20
    },
]

def add_category(name, parent_id=None):
    try:
        connection = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port="5432",
                                  database=config.DB_NAME)
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO Categories (name, parent_id) VALUES (%s,%s)"""
        record_to_insert = (name, parent_id)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully Categories table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record Categories table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def add_category_to_db():
    for category in categories:
        add_category(name=category.get("name"), parent_id=category.get("parent_id"))




products = [
    {
        "name": "",
        "description": "",
        "imag_url": "",
        "price": 0,
        "category_id": 0
    }
]




def add_product(name, description, image_url, price, category_id):
    try:
        connection = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port="5432",
                                  database=config.DB_NAME)
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO Products (name, description, image_url, price, category_id) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (name, description, image_url, price, category_id)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully Products table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record Products table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def add_products_to_db():
    for product in products:
        add_category(name=product.get("name"), description=product.get("description"), image_url=product.get("image_url"), price=product.get("price"), category_id=product.get("category.id"))      