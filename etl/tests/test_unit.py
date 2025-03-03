import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from srm.postgres import get_postgres_count, insert_data_to_postgresql
from srm.google_sheets import get_data_from_google_sheets

class TestPostgresCount(unittest.TestCase):
    @patch('srm.postgres.psycopg2.connect')
    def test_get_postgres_count(self, mock_connect):
        # Создаем мок курсора
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (5,)  # Имитируем результат COUNT(*)

        # Настроим мок соединения, чтобы он возвращал мок курсора
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection

        # Вызываем тестируемую функцию
        count = get_postgres_count()

        # Проверяем, что функция вернула правильное значение
        self.assertEqual(count, 5)

        # Проверяем, что методы были вызваны правильно
        mock_cursor.execute.assert_called_once_with("SELECT COUNT(*) FROM orders1;")
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()


class TestInsertDataToPostgresql(unittest.TestCase):
    @patch('srm.postgres.psycopg2.connect')
    def test_insert_data_to_postgresql(self, mock_connect):
        # Создаем мок курсора
        mock_cursor = MagicMock()

        # Настроим мок соединения, чтобы он возвращал мок курсора
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection

        # Подготовим тестовые данные
        test_data = [
            {
                'Отметка времени': '01.01.2023 12:00:00',
                'Имя': 'John Doe',
                'Телефон': '+79991234567',
                'Полное название школы (как будет подписана на обложке)': 'School 1',
                'Класс, литер': '10A',
                'Размер альбома': 'Large',
                'Количество альбомов': '10',
                'Желаемая дата съемки': '01.02.2023',
                'Выберите место съемки. Здесь самые популярные студии, в которых мы гарантируем отличный результат.': 'Studio A',
                'Выберите дизайн обложки (максимум 2)': 'Design 1',
                'Какого цвета альбом будет внутри?': 'Blue',
                'Выберите с каким светом снимаем портрет': 'Natural',
                'Как оформим первый разворот?': 'Option 1',
                'Нужен ли альбом учителю?': 'Да',
                'Откуда узнали о нас?': 'Internet',
                'Дополнительная информация': 'None'
            }
        ]

        # Вызываем тестируемую функцию
        insert_data_to_postgresql(test_data)

        # Проверяем, что SQL-запрос был выполнен правильно
        expected_query = """
        INSERT INTO orders1 (
            timestamp, name, phone, school_name, class, album_size, album_count, shooting_date,
            studio, cover_design, album_color, portrait_light, first_spread, teacher_album,
            how_found, additional_info
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        expected_values = (
            datetime(2023, 1, 1, 12, 0), 'John Doe', '+79991234567', 'School 1', '10A', 'Large', '10',
            datetime(2023, 2, 1), 'Studio A', 'Design 1', 'Blue', 'Natural', 'Option 1', True, 'Internet', 'None'
        )
        mock_cursor.execute.assert_called_once_with(expected_query, expected_values)

        # Проверяем, что изменения были сохранены
        mock_connection.commit.assert_called_once()

        # Проверяем закрытие курсора и соединения
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()


class TestGetDataFromGoogleSheets(unittest.TestCase):
    @patch('srm.google_sheets.client.open')
    def test_get_data_from_google_sheets(self, mock_open):
        # Создаем мок листа
        mock_sheet = MagicMock()
        mock_sheet.get_all_records.return_value = [
            {'Отметка времени': '01.01.2023 12:00:00', 'Имя': 'Alice'},
            {'Отметка времени': '02.01.2023 12:00:00', 'Имя': 'Bob'}
        ]

        # Настроим мок клиента, чтобы он возвращал мок листа
        mock_workbook = MagicMock()
        mock_workbook.sheet1 = mock_sheet
        mock_open.return_value = mock_workbook

        # Вызываем тестируемую функцию
        data = get_data_from_google_sheets()

        # Проверяем, что функция вернула правильные данные
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['Имя'], 'Alice')
        self.assertEqual(data[1]['Имя'], 'Bob')

        # Проверяем, что методы были вызваны правильно
        mock_open.assert_called_once_with("DAPcoppi")
        mock_sheet.get_all_records.assert_called_once()


if __name__ == '__main__':
    unittest.main()