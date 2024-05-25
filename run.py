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
gardenplant = SHEET.worksheet('gardenplant')
houseplants = SHEET.worksheet('houseplants')
flowerslist = SHEET.worksheet('flowerslist')
hp_list = SHEET.worksheet('hp_list')
gp_list = SHEET.worksheet('gp_list')


BRIGHT_GREEN = "\033[92m"
BRIGHT_BLUE = "\033[94m"
RESET = "\033[0m"

def clear_screen():
    """
    clears console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


BRIGHT_GREEN = "\033[92m"
BRIGHT_BLUE = "\033[94m"
RESET = "\033[0m"

def welcome_message():
    """
    Displays the welcome message only once at the start of the program.
    """
    clear_screen()

# print(r"""
#       __      __   _                    _
#       \ \    / /__| |__ ___ _ __  ___  | |_ ___
#        \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \
#         \_/\_/\___|_\__\___/_|_|_\___|  \__\___/
#     """)
    
FLOWER = r"""
        _
      _(_)_                          wWWWw   _
     (_)@(_)   vVVVv     _     @@@@  (___) _(_)_
       (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)
        `  |/    Y    (_)@(_)  @@@@   \|/   (_)\
          \|    \|/    /(_)    \|      |/      |
           | / \ | /  \|/       |/    \|      \|/
        \\\|//\\\|/// \|///  \\\|//  \\|//  \\\|//
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    
BANNER = r"""
      ___ _                          __           _    _  __
     | __| |_____ __ _____ _ _ ___  / _|___ _ _  | |  (_)/ _|___
     | _|| / _ \ V  V / -_) '_(_-< |  _/ _ \ '_| | |__| |  _/ -_)
     |_| |_\___/\_/\_/\___|_| /__/ |_| \___/_|   |____|_|_| \___|
    """

print(f"{BRIGHT_GREEN}{FLOWER}{RESET}")
print(f"{BRIGHT_BLUE}{BANNER}{RESET}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
input("Press (Enter) to go to the main menu\n")


def main_menu():
    """
    Displays main menu, options 1-4
    """
    clear_screen()
    GREEN = "\033[92m"
    RESET = "\033[0m"
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print(f"{GREEN}1. View Current Stock{RESET}")
    print(f"{GREEN}2. Add Stock{RESET}")
    print(f"{GREEN}3. Deduct Stock{RESET}")
    print(f"{GREEN}4. Update Plants{RESET}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        option = input(
            "Please select an option from 1-4 and press enter:\n"
            ).strip()

        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                break
            else:
                print(
                    "Invalid Input!\n"
                    "Please enter a number between 1 & 4 and press enter\n")
        else:
            print(
                "Invalid Input!\n"
                "Please enter a number between 1 & 4 and press enter\n")

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
        print("Update Plants")
        update_plants_menu()
    else:
        print("Invalid Choice!\n Please enter a number between 1 & 4\n")


def submenu_current():
    """
    Displays the submenu for View Current Stock and handles user input.
    """
    clear_screen()
    BLUE = "\033[94m"
    RESET = "\033[0m"
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print(f"{BLUE}View Current Stock{RESET}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("1. Flowers")
    print("2. Gardenplant")
    print("3. Houseplants")
    print("4. Return to Main Menu\n")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        option = input(
             "Please select an option from 1-4 and press enter:\n"
        ).strip()
        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                if option == 1:
                    menu_category("flowers", flowers)
                elif option == 2:
                    menu_category("gardenplant", gardenplant)
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
    BLUE = "\033[94m"
    RESET = "\033[0m"
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"{BLUE}Add Stock{RESET}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("1. Flowers")
    print("2. Gardenplant")
    print("3. Houseplants")
    print("4. Return to Main Menu")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        option = input(
             "Please select an option from 1-4 and press enter:\n"
        ).strip()

        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                if option == 1:
                    add_stock(flowers, "flower")
                elif option == 2:
                    add_stock(gardenplant, "gardenplant")
                elif option == 3:
                    add_stock(houseplants, "houseplant")
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
    BLUE = "\033[94m"
    RESET = "\033[0m"
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"{BLUE}Add Stock{RESET}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    while True:
        item_name = input(
         f"Enter {category_name} name, "
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
                print(f"Item '{item_name}' not found in the list.")
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
    print("1. Flowers")
    print("2. Gardenplant")
    print("3. Houseplants")
    print("4. Return to Main Menu")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        option = input(
             "Please select an option from 1-4 and press enter:\n"
             ).strip()

        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                if option == 1:
                    use_stock(flowers, "flowers")
                elif option == 2:
                    use_stock(gardenplant, "gardenplant")
                elif option == 3:
                    use_stock(houseplants, "houseplants")
                elif option == 4:
                    print("Returning to Main Menu")
                    main_menu()
                    return
            else:
                print("Invalid Choice. Please enter a number between 1 & 4:\n")
        else:
            print("Invalid Input. "
                  "Please enter a valid number between 1 & 4:\n")


def use_stock(inventory_sheet, category_name):
    """
    Uses stock from a specific category.

    Args:
       inventory_sheet (Worksheet): Inventory data worksheet.

        category_name (str): The name of the category.
    """
    clear_screen()
    BLUE = "\033[94m"
    RESET = "\033[0m"
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"{BLUE}Deduct Stock{RESET}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    while True:
        item_name = input(
         f"Please enter {category_name} name, "
         f"or type 'exit' to go back to menu:\n"
        ).lower()
        if item_name == "exit":
            use_stock_menu()
            return

        amount_to_use = input("Please enter the amount to use:\n")

        if amount_to_use.isdigit():
            amount_to_use = int(amount_to_use)
            cell = inventory_sheet.find(item_name.title())
            if cell:
                current_amount = int(
                 inventory_sheet.cell(cell.row, cell.col + 1).value)

                if current_amount >= amount_to_use:
                    new_amount = current_amount - amount_to_use
                    inventory_sheet.update_cell(
                     cell.row, cell.col + 1, new_amount)
                    print(f"Used {amount_to_use} from {item_name}. "
                          f"New amount: {new_amount}")
                else:
                    print("Error: Insufficient stock.")
            else:
                print(f"Item '{item_name}' not found in the category.")
        elif amount_to_use.lower() == "exit":
            use_stock_menu()
            return
        else:
            print("Invalid input for amount. Please enter a valid number.")


def update_plants_menu():
    """
    Displays the submenu for View Current Stock and handles user input.
    """
    clear_screen()
    BLUE = "\033[94m"
    RESET = "\033[0m"
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print(f"{BLUE}Update Plants{RESET}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("1. View Plants List")
    print("2. Add New Plant")
    print("3. Remove Existing Plant")
    print("4. Return to Main Menu")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        option = input(
             "Please select an option from 1-4 and press enter:\n"
             ).strip()
        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                if option == 1:
                    plants_list_menu()
                if option == 2:
                    update_new_plant()
                elif option == 3:
                    remove_plant()
                elif option == 4:
                    clear_screen()
                    main_menu()
                    break
            else:
                print(f"Invalid Input! Please enter a number between 1 and 4.")
        else:
            print("Invalid Input!\nPlease enter a number between 1 and 4.\n")


def plants_list_menu():
    """
    Displays the list of plants menu
    """
    clear_screen()
    BLUE = "\033[94m"
    RESET = "\033[0m"
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print(f"{BLUE}View Plants List{RESET}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("1. Flowers List")
    print("2. Garden Plants List")
    print("3. House Plants List")
    print("4. Go Back\n")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        option = input(
             "Please select an option from 1-4 and press enter:\n"
             ).strip()
        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                if option == 1:
                    menu_category_list("flowers list", flowerslist)
                elif option == 2:
                    menu_category_list("gardenplant list", gp_list)
                elif option == 3:
                    menu_category_list("houseplants list", hp_list)
                elif option == 4:
                    clear_screen()
                    update_plants_menu()
                    break
            else:
                print(f"Invalid Input! Please enter a number between 1 and 4.")
        else:
            print("Invalid Input!\nPlease enter a number between 1 and 4.\n")


def menu_category_list(category_name, category_sheet):
    """
    Displays the plant list in their specific category.
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
        print("{:<20}".format(row[0]))
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    input("Press 'Enter' to return to the plant list Menu\n")
    clear_screen()
    plants_list_menu()
    clear_screen()


def update_new_plant():
    """
    Displays the menu for updating new items and handles user input.
    """
    clear_screen()
    BLUE = "\033[94m"
    RESET = "\033[0m"
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"{BLUE}Add New Plant{BLUE}")
    print("--------------------------------------------------\n")
    print("1. Flowers")
    print("2. Gardenplant")
    print("3. Houseplants")
    print("4. Go Back")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        option = input(
             "Please select an option from 1-4 and press enter:\n"
             ).strip()

        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                if option == 1:
                    update_list(flowers, flowerslist, "flower", "add")
                elif option == 2:
                    update_list(gardenplant, gp_list, "gardenplant", "add")
                elif option == 3:
                    update_list(houseplants, hp_list, "houseplant", "add")
                elif option == 4:
                    print("Go Back")
                    update_plants_menu()
                    break
            else:
                print("Invalid Choice. Please enter a number between 1 & 4\n")
        else:
            print("Invalid Input. Please enter a valid number between 1 & 4\n")


def update_list(in_sheet, category_sheet, category_name, action):
    """
    in_sheet (inventory sheet) - stock sheet
    category_sheet - list sheet
    category_name  - name of the stock sheet

    Adds stock to a specific category.

    Args:
       in_sheet (Worksheet): Holds the inventory data.

        category_name (str): The name of the category.
    """
    clear_screen()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Update Plants")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        item_name = input(
         f"Enter {category_name} name, "
         f"or 'exit' to go back:\n"
        ).lower()

        if item_name == "exit":
            update_new_plant()
            return
        if action == "add":
            cell = in_sheet.find(item_name.title())
            cellList = category_sheet.find(item_name.title())

            if cell and cellList:
                print(f"{item_name.title()} already exists in current stock")
            elif not cell and cellList:
                amount_to_add = input("Enter the amount to add:\n").strip()

                if amount_to_add.isdigit():
                    amount_to_add = int(amount_to_add)
                    in_sheet.append_row([item_name.title(), amount_to_add])
                    print(f"Added {amount_to_add} to {item_name}. ")
            else:
                print(f"Entered item {item_name} is invalid.")
        elif action == "remove":
            cell = in_sheet.find(item_name.title())
            if cell:
                in_sheet.delete_rows(cell.row)
                print(f"{item_name} is deleted")
            else:
                print(f"{item_name} is not found in the list")


def remove_plant():
    """
    Displays the menu for removing item from the list
    """
    clear_screen()
    BLUE = "\033[94m"
    RESET = "\033[0m"
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"{BLUE}Remove Existing Plant{BLUE}")
    print("--------------------------------------------------\n")
    print("1. Flowers")
    print("2. Gardenplant")
    print("3. Houseplants")
    print("4. Go Back")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    while True:
        option = input(
             "Please select an option from 1-4 and press enter:\n"
            ).strip()

        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                if option == 1:
                    update_list(flowers, flowerslist, "flower", "remove")
                elif option == 2:
                    update_list(gardenplant, gp_list, "garden_plant", "remove")
                elif option == 3:
                    update_list(houseplants, hp_list, "houseplant", "remove")
                elif option == 4:
                    print("Go Back")
                    update_plants_menu()
                    break
            else:
                print("Invalid Choice. Please enter a number between 1 & 4\n")
        else:
            print("Invalid Input. Please enter a valid number between 1 & 4\n")


if __name__ == '__main__':
    welcome_message()
    main_menu()
