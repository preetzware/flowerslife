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

def main_menu () :
  """
  Displays main menu, options 1-4
  """
  clear_screen ()
  print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
  print("1. View Current Stock")
  print("2. Add Stock")
  print("3. Deduct Stock")
  print("4. Input New Plants")
  print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

  while True:
        option = input("Please select an option from 1-4:\n").strip()  # Trim

        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                break
            else:
                print("Invalid Input!\n Please enter a number between 1 & 4\n")
        else:
            print("Invalid Input!\n Please enter a number between 1 & 4\n")

if option == 1:
    print("View Current Stock:")
    submenu_current()
elif option == 2:
    print("Add Stock")
    input_new_menu()
elif option == 3:
    print("Deduct Stock")
    use_stock_menu()
elif option == 4:
    print("Input New Plants")
    update_new_plant()
else:
    print("Invalid Choice!\n Please enter a number between 1 & 4\n")


if __name__ == '__main__':
    welcome_message()
    main_menu()