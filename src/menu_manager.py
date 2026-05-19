# menu_manager.py

import functions as f

def main(df):
    while True:
        f.clear_console()
        print("Main Menu")
        print("1. Overview of Economy")
        print("2. Generate Report")
        print("3. Rank Economies by Year")
        print("4. Back Testing")
        print("5. Compare Countries")
        print("6. Check Modules")
        print("7. Exit")

        func_choice = input("Enter your choice: ")

        if func_choice == "1":
            f.choice_1(df)
        elif func_choice == "2":
            country = input("Enter the country for the report (default: India): ") or "India"
            f.choice_2(df, country=country)

        elif func_choice == "3":
            
            year = input("Enter the year to rank economies (e.g., 2005): ") or 2005
            f.rank_economies(df, year=int(year))
            input("\nPress Enter to return to the menu...")

        elif func_choice == "4":
            f.choice_3(df)

        elif func_choice == "5":
            f.choice_4(df)


        elif func_choice == "6":
            f.choice_5(df)
        elif func_choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            input("Press Enter to return to the menu...")



if __name__ == "__main__":  
    from data_pipeline import df
    while True:
        try:
            main(df) 
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to return to the menu...")











