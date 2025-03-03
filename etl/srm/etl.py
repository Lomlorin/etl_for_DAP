import time
from .google_sheets import get_data_from_google_sheets
from .postgres import get_postgres_count, insert_data_to_postgresql
from .utils import parse_record

def update_database_periodically():
    """Основной цикл для проверки и добавления данных."""
    while True:
        try:
            data_from_sheet = get_data_from_google_sheets()
            google_sheet_count = len(data_from_sheet)
            print(f"Количество записей в Google Sheets: {google_sheet_count}")

            postgres_count = get_postgres_count()
            print(f"Количество записей в PostgreSQL: {postgres_count}")

            if google_sheet_count == postgres_count:
                print("Таблица актуальна!")
            elif google_sheet_count > postgres_count:
                print("Найдены новые записи. Добавляем их в PostgreSQL...")
                new_data = [parse_record(record) for record in data_from_sheet[postgres_count:]]
                insert_data_to_postgresql(new_data)
                print("Теперь таблица актуальна!")

        except Exception as error:
            print(f"Ошибка в цикле обновления: {error}")

        time.sleep(3600)

if __name__ == "__main__":
    update_database_periodically()