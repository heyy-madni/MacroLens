# menu_manager.py


import functions as f

def main(df):
    while True:
        f.clear_console()
        print("Main Menu")
        print("1. Overview of Economy")
        print("2. Generate Report")
        print("3. Back Testing")
        print("4. Compare Countries")
        print("5. Check Modules")
        print("6. Exit")

        func_choice = input("Enter your choice: ")

        if func_choice == "1":
            f.choice_1(df)
        elif func_choice == "2":
            country = input("Enter the country for the report (default: India): ") or "India"
            f.choice_2(df, country=country)
        elif func_choice == "3":
            f.choice_3(df)
        elif func_choice == "4":
            f.choice_4(df)
        elif func_choice == "5":
            f.choice_5(df)
        elif func_choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            input("Press Enter to return to the menu...")













