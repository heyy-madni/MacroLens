def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


from report_genrator import  genrate_report,over_view_of_economy_chart
from data_manager import back_testing ,compare_countries,df,regime_periods

# function_map = {
#     "1": over_view_of_economy_chart,
#     "2": genrate_report,
#     "3": back_testing,
#     "4":compare_countries,
#     #todo
#     "5": lambda: print("add this madni"),
    
#     "6": exit
    
# }

def choice_1():
    clear_console()
    country = input("Enter the country for overview (default: India): ")
    if country == "india"or country == "India" or not country:
        country = "India"
    elif country == "usa" or country == "US"or country == "USA" or country == "united states":
        country = "USA"
    elif country == "china"or country == "China":
        country = "China"
          
    if not country:
        print(" entered country not found. Defaulting to India.")
              
    clear_console()
    over_view_of_economy_chart(choice=country)
    input("Press Enter to return to the menu...")
    clear_console()


def choice_2():
    clear_console()
    genrate_report()
    input("Press Enter to return to the menu...")
    clear_console()

def choice_3():
    clear_console()
    print("Back Testing Options:")
    print("1. Custom Year Back Testing")
    print("2. Regime Periods")
    print("3. Condition Checker")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        year = int(input("Enter the year for back testing: "))
        back_testing(year)
    elif choice == "2":
        country = input("Enter the country for regime periods (default: India): ")
        if country == "india"or country == "India" or not country:
            country = "India"
        elif country == "usa" or country == "US"or country == "USA" or country == "united states":
            country = "USA"
        elif country == "china"or country == "China":
            country = "China"
        regime_periods(country)
    elif choice == "3":
        print(df[["Year", "Country", "Condition", "Condition_checker"]].to_string())
        pass
    else:
        print("Invalid choice. Returning to menu.")
    input("Press Enter to return to the menu...")
    clear_console()

def choice_4():
    clear_console()
    year = int(input("Enter the year for comparison: "))
    clear_console()
    compare_countries(country1 =df["Country"].unique()[0], country2 =df["Country"].unique()[1], country3 =df["Country"].unique()[2], year=year)
    input("Press Enter to return to the menu...")
    clear_console()












