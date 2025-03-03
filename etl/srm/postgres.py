import psycopg2
from .config import POSTGRES_CONFIG

def get_postgres_count():
    """Получение количества записей в таблице orders1."""
    try:
        connection = psycopg2.connect(**POSTGRES_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM orders1;")
        count = cursor.fetchone()[0]
        return count
    except Exception as error:
        print(f"Ошибка при подключении к PostgreSQL: {error}")
        return 0
    finally:
        if connection:
            cursor.close()
            connection.close()

def insert_data_to_postgresql(data):
    """Вставка данных в таблицу orders1."""
    try:
        connection = psycopg2.connect(**POSTGRES_CONFIG)
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO orders1 (
            timestamp, name, phone, school_name, class, album_size, album_count, shooting_date,
            studio, cover_design, album_color, portrait_light, first_spread, teacher_album,
            how_found, additional_info
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        for record in data:
            cursor.execute(insert_query, (
                record['timestamp'], record['name'], record['phone'], record['school_name'],
                record['class'], record['album_size'], record['album_count'], record['shooting_date'],
                record['studio'], record['cover_design'], record['album_color'], record['portrait_light'],
                record['first_spread'], record['teacher_album'], record['how_found'], record['additional_info']
            ))

        connection.commit()
        print("Данные успешно добавлены в базу данных!")
    except Exception as error:
        print(f"Ошибка при добавлении данных: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()