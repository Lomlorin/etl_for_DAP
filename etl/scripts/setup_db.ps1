# Настройки подключения к PostgreSQL
$DB_NAME = "test"
$DB_USER = "postgres"
$DB_PASSWORD = "polina"

# Создание пользователя и базы данных
Write-Output "Создание базы данных $DB_NAME..."
psql -U postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
psql -U postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"

# Создание таблицы orders1
psql -U $DB_USER -d $DB_NAME -c @"
CREATE TABLE IF NOT EXISTS orders1 (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    name VARCHAR(255),
    phone VARCHAR(20),
    school_name VARCHAR(255),
    class VARCHAR(10),
    album_size VARCHAR(50),
    album_count INTEGER,
    shooting_date DATE,
    studio VARCHAR(255),
    cover_design VARCHAR(255),
    album_color VARCHAR(50),
    portrait_light VARCHAR(50),
    first_spread VARCHAR(255),
    teacher_album BOOLEAN,
    how_found VARCHAR(255),
    additional_info TEXT
);
"@

if ($?) {
    Write-Output "База данных успешно настроена."
} else {
    Write-Output "Ошибка при создании базы данных."
    exit 1
}