from functions import (
    choice_1, choice_2, choice_3, choice_5,
    compare_countries, clear_console
)
from data_pipeline import df

def handle_compare():
    clear_console()
    country1 = input("Enter the first country (default: India): ") or "India"
    country2 = input("Enter the second country (default: USA): ") or "USA"
    country3 = input("Enter the third country (default: China): ") or "China"
    Years_input = input("Enter the Years for comparison (default: 2020): ")
    Years = int(Years_input) if Years_input else 2020

    clear_console()
    for line in compare_countries(country1, country2, country3, Years):
        print(line)
    input("Press Enter to return to the menu...")

def menu():
    clear_console()
    print("Main Menu")
    print("1. Overview of Economy")
    print("2. Generate Report")
    print("3. Back Testing")
    print("4. Compare Countries")
    print("5. Check Modules")
    print("6. Exit")

    func_choice = input("Enter your choice: ")

    if func_choice == "1":
        choice_1(df)
    elif func_choice == "2":
        country = input("Enter the country for the report (default: India): ") or "India"
        choice_2(df, country=country)
        
    elif func_choice == "3":
        choice_3(df)
    elif func_choice == "4":
        handle_compare()
    elif func_choice == "5":
        choice_5(df)
    elif func_choice == "6":
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
        input("Press Enter to return to the menu...")














