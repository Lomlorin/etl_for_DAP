import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .config import GOOGLE_SHEETS_CREDENTIALS, GOOGLE_SHEETS_SCOPE, GOOGLE_SHEETS_NAME

def authorize_google_sheets():
    """Авторизация в Google Sheets API."""
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_CREDENTIALS, GOOGLE_SHEETS_SCOPE)
    client = gspread.authorize(creds)
    return client

def get_data_from_google_sheets():
    """Получение данных из Google Sheets."""
    client = authorize_google_sheets()
    sheet = client.open(GOOGLE_SHEETS_NAME).sheet1
    return sheet.get_all_records()