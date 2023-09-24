import psycopg2
from data import config

categories = [
    {
        "name": "🎧 Электроника"
    },
    {
        "name": "🔌 Бытовая техника"
    },
    {
        "name": "👕 Одежда"
    },
    {
        "name": "👟 Обувь"
    },
    {
        "name": "🎒 Аксессуары"
    },
    {
        "name": "💄 Красота"
    },
    {
        "name": "❤️ Здоровье"
    },
    {
        "name": "🏠 Товары для дома"
    },
    {
        "name": "🧱 Строительство и ремонт"
    },
    {
        "name": "🚘 Автотовары"
    },
    {
        "name": "🧸 Детские товары"
    },
    {
        "name": "🎨 Хобби и творчество"
    },
    {
        "name": "🏀 Спорт и отдых"
    },
    {
        "name": "🍏 Продукты и питания"
    },
    {
        "name": "🧴 Бытовая химия и личная гигиена"
    },
    {
        "name": "📔 Канцтоварые"
    },
    {
        "name": "🐾 Зоотовары"
    },
    {
        "name": "📖 Книги"
    },
    {
        "name": "🍃 Дачаб сад и огород"
    },
    {
        "name": "Смартфоны и телефоны",
        "parent_id": 1
    },
    {
        "name": "Умные часы и фитнес браслеты",
        "parent_id": 1
    },
    {
        "name": "Ноутбуки, планшеты и электронные книги",
        "parent_id": 1
    },
    {
        "name": "Комьютерная техника",
        "parent_id": 1
    },
    {
        "name": "Наушники и аудиотехники",
        "parent_id": 1
    },
    {
        "name": "Фото и фидеотехника",
        "parent_id": 1
    },
    {
        "name": "Часы и электронные будильники",
        "parent_id": 1
    },
    {
        "name": "Умный дом и безопасность",
        "parent_id": 1
    },
    {
        "name": "Телевизоры и видеотехника",
        "parent_id": 1
    },
    {
        "name": "Квадрокоптеры и аксессуары",
        "parent_id": 1
    },
    {
        "name": "Игровые приставки",
        "parent_id": 1
    },
    {
        "name": "Навигаторы",
        "parent_id": 1
    },
    {
        "name": "Офисная техника",
        "parent_id": 1
    },
    {
        "name": "Оптические приборы",
        "parent_id": 1
    },
    {
        "name": "Аксессуары для электроники",
        "parent_id": 1
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

# add_category_to_db():
      