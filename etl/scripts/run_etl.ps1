# Путь к основному файлу ETL
$ETL_SCRIPT = "..\srm\etl.py"

# Запуск ETL-процесса
Write-Output "Запуск ETL-процесса..."
python $ETL_SCRIPT

if ($?) {
    Write-Output "ETL-процесс успешно завершен."
} else {
    Write-Output "Ошибка при выполнении ETL-процесса."
    exit 1
}