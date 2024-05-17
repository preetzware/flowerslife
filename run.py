import gspread
from google.oauth2.service_account import Credentials
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('flowers_for_life')

flowers = SHEET.worksheet('flowers')
garden_plants = SHEET.worksheet('garden_plants')
houseplants = SHEET.worksheet('houseplants')
flowerslist = SHEET.worksheet('flowerslist')
hp_list = SHEET.worksheet('hp_list')
gp_list = SHEET.worksheet('gp_list')


def clear_screen():
    """
    clears console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')