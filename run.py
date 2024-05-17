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

def welcome_message():
    """
    Displays the welcome message.
    """
    clear_screen()

    print(r"""
    
       __       __)
      (, ) |  /     /)
        | /| /  _  // _  ______    _    _/_ ___
        |/ |/ _(/_(/_(__(_) // (__(/_   (__(_)
        /  |                                                         
""")
   

    FLOWER = r""" 
        _
      _(_)_                          wWWWw   _
     (_)@(_)   vVVVv     _     @@@@  (___) _(_)_
       (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)
        `  |/    Y    (_)@(_)  @@@@   \|/   (_)\
          \|    \|/    /(_)    \|      |/      |
           | / \ | /  \|/       |/    \|      \|/
        \\\|//\\\|/// \|///  \\\|//  \\|//  \\\|// 
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """

    BANNER = r"""
        ________)                                          _            
      (, /     /)                        /)           ___/__) ,   /)   
        /___, // ____   _  _  __  _     // _____     (, /        //  _ 
    ) /     (/_(_) (_(/ _(/_/ (_/_)_  /(_(_)/ (_      /    _(_ /(__(/_
    (_/                               /)              (_____   /)      
                                    (/                      )(/  
    """

    # Print FLOWER and BANNER
    print(FLOWER)
    print(BANNER)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    input("Press (Enter) to go to the main menu\n")



if __name__ == '__main__':
    welcome_message()
    main_menu()