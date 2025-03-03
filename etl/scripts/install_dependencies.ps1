# Установка зависимостей
Write-Output "Установка зависимостей..."
python -m pip install --upgrade pip
pip install -r ..\requirements.txt

if ($?) {
    Write-Output "Зависимости успешно установлены."
} else {
    Write-Output "Ошибка при установке зависимостей."
    exit 1
}