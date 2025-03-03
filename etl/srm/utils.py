from datetime import datetime

def parse_record(record):
    """Преобразование данных из Google Sheets в формат для PostgreSQL."""
    return {
        'timestamp': datetime.strptime(record['Отметка времени'], "%d.%m.%Y %H:%M:%S"),
        'name': record['Имя'],
        'phone': record['Телефон'],
        'school_name': record['Полное название школы (как будет подписана на обложке)'],
        'class': record['Класс, литер'],
        'album_size': record['Размер альбома'],
        'album_count': record['Количество альбомов'],
        'shooting_date': datetime.strptime(record['Желаемая дата съемки'], "%d.%m.%Y"),
        'studio': record['Выберите место съемки. Здесь самые популярные студии, в которых мы гарантируем отличный результат.'],
        'cover_design': record['Выберите дизайн обложки (максимум 2)'],
        'album_color': record['Какого цвета альбом будет внутри?'],
        'portrait_light': record['Выберите с каким светом снимаем портрет'],
        'first_spread': record['Как оформим первый разворот?'],
        'teacher_album': record['Нужен ли альбом учителю?'] == 'Да',
        'how_found': record['Откуда узнали о нас?'],
        'additional_info': record['Дополнительная информация']
    }