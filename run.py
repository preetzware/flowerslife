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

def submenu_current():
    """
    Displays the submenu for View Current Stock and handles user input.
    """
    clear_screen()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("View Current Stock")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("1. flowers")
    print("2. garden_plants")
    print("3. houseplants")
    print("4. Return to Main Menu\n")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        option = input("Please select an option from 1-4:\n").strip()
        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                if option == 1:
                    menu_category("flowers", flowers)
                elif option == 2:
                    menu_category("garden_plants", garden_plants)
                elif option == 3:
                    menu_category("houseplants", houseplants)
                elif option == 4:
                    clear_screen()
                    main_menu()
                    break
            else:
                print(f"Invalid Input! Please enter a number between 1 and 4.")
        else:
            print("Invalid Input!\nPlease enter a number between 1 and 4.\n")

def menu_category(category_name, category_sheet):
    """
    Displays the plant items in their specific category.
    Args:
        category_name (str): The name of the category.
        category_sheet (Worksheet): The worksheet containing the category data.
    """
    clear_screen()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(category_name)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    data = category_sheet.get_all_values()
    
    for row in data:
        print("{:<20} {:<20}".format(row[0], row[1]))
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    input("Press 'Enter' to return to the Current Stock Menu\n")
    clear_screen()
    submenu_current()
    clear_screen()

def input_new_menu():
    """
    Displays the menu for inputting new items and handling user input.
    """
    clear_screen()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"{BLUE}Input New Plants{RESET}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("1. flowers")
    print("2. garden_plants")
    print("3. houseplants")
    print("4. Return to Main Menu")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        option = input("Please select an option from 1-4:\n").strip()

        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                if option == 1:
                    add_stock(flowers, "flowers")
                elif option == 2:
                    add_stock(garden_plants, "garden_plants")
                elif option == 3:
                    add_stock(houseplants, "houseplants")
                elif option == 4:
                    print("Return to Main Menu")
                    main_menu()
                    break
            else:
                print("Invalid Choice. Please enter a number between 1 & 4\n")
        else:
            print("Invalid Input. Please enter a valid number between 1 & 4\n")

def add_stock(inventory_sheet, category_name):
    """
    Adds stock to a specific category.

    Args:
       inventory_sheet (Worksheet): Holds the inventory data.

        category_name (str): The name of the category.
    """
    clear_screen()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"{BLUE}Add Stock{RESET}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    while True:
        item_name = input(
         f"Enter {category_name} item name, "
         f"or 'exit' to return to the menu:\n"
        ).lower()

        if item_name == "exit":
            input_new_menu()
            return

        amount_to_add = input("Please enter the amount to add:\n").strip()

        if amount_to_add.isdigit():
            amount_to_add = int(amount_to_add)
            cell = inventory_sheet.find(item_name.title())
            if cell:
                current_amount = int(
                 inventory_sheet.cell(cell.row, cell.col + 1).value)

                new_amount = current_amount + amount_to_add
                inventory_sheet.update_cell(cell.row, cell.col + 1, new_amount)
                print(f"Added {amount_to_add} to {item_name}. "
                      f"New amount: {new_amount}")

            else:
                print(f"Item '{item_name}' not found in the category.")
        elif amount_to_add.lower() == "exit":
            input_new_menu()
            return
        else:
            print("Invalid input for amount. Please enter a valid number.")

def use_stock_menu():
    """
    Displays the menu for using/deducting stock items and handling user input.
    """
    clear_screen()
    BLUE = "\033[94m"
    RESET = "\033[0m"
    
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"{BLUE}Deduct Stock{RESET}")
    print("--------------------------------------------------\n")
    print("1. flowers")
    print("2. garden_plants")
    print("3. houseplants")
    print("4. Return to Main Menu")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")



if __name__ == '__main__':
    welcome_message()
    main_menu()