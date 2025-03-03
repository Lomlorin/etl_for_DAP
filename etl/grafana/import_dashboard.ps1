# Настройки Grafana
$GRAFANA_URL = "http://localhost:3000"
$API_KEY = "sa-1-api-37ddea15-8f7d-4e2a-ad60-0b14383631e2"

# Путь к файлу дашборда
$DASHBOARD_FILE = Resolve-Path ".\dashboard.json"

# Читаем содержимое файла
$dashboardJson = Get-Content $DASHBOARD_FILE | Out-String

# Создаем тело запроса
$body = @{
    dashboard = ($dashboardJson | ConvertFrom-Json)
    overwrite = $true
} | ConvertTo-Json -Depth 10

# Импортируем дашборд
Invoke-RestMethod -Uri "$GRAFANA_URL/api/dashboards/db" -Method Post -Headers @{"Authorization" = "Bearer $API_KEY"} -Body $body -ContentType "application/json"

if ($?) {
    Write-Output "Дашборд успешно импортирован."
} else {
    Write-Output "Ошибка при импорте дашборда."
    exit 1
}