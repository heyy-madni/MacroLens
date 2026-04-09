from report_genrator import genrate_report,over_view_of_economy_chart
from data_manager import back_testing ,compare_countries



function_map = {
    "1": over_view_of_economy_chart,
    "2": genrate_report,
    "3": back_testing,
    "4":compare_countries,
    #todo
    "5": lambda: print("Report of specific years function not implemented yet."),
    "6": exit
    
}







def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')



def menu():
    # while True:
        clear_console()
        print("Welcome to the India Economy Health Checker!")
        print("Please select an option:")
        print("1. Function Menu")
        print("2. Exit")
        # print("3. Back Testing")
        # print("4. Exit")


        choice = input("Enter your choice: ")
        
        if choice == '1':
            clear_console()
            print("function menu")
            print("1. over view of economy ")
            print("2. Generate Report")
            print("3. Back Testing")
            print("4. Compare Countries") 
            print("5.report of a specific years")
            print("6. Exit")
            
            func_choice = input("Enter your choice: ")
           
            if func_choice == "1":
                    clear_console()
                    country = input("Enter the country for overview (default: India): ")
                    if country == "india"or country == "India" or not country:
                        country = "India"
                    elif country == "usa" or country == "US"or country == "USA" or country == "united states":
                        country = "United States"
                    elif country == "china"or country == "China":
                        country = "China"
                          
                    if not country:
                        print(" entered country not found. Defaulting to India.")
              
                    clear_console()
                    function_map[func_choice](choice=country)
                    input("Press Enter to return to the menu...")
                    clear_console()


            elif func_choice == "2":
                    clear_console()
                    function_map[func_choice]()
                    input("Press Enter to return to the menu...")
                    clear_console()

            elif func_choice == '3':
                    clear_console()
                    years = input(("Enter 4 years for back testing (comma separated, e.g. 2008,2009,2020,2021): "))
                    year_list = [int(year.strip()) for year in years.split(",")]
                    if len(year_list) != 4:
                        print("Please enter exactly 4 years.")
                        input("Press Enter to try again...")
                        clear_console()
                        return
                    clear_console()
                    function_map[func_choice](*year_list)
                    input("Press Enter to return to the menu...")
                    clear_console()
           
            elif func_choice == '4':
                    clear_console()
                    country1 = input("Enter the first country: ")
                    country2 = input("Enter the second country: ")
                    year = int(input("Enter the year for comparison: "))
                    clear_console()
                    function_map[func_choice](country1, country2, year)
                    input("Press Enter to return to the menu...")
                    clear_console()
           
            else:
                    function_map[func_choice]()
                    input("Press Enter to return to the menu...")
                    clear_console()






        # if choice == '1':
        #     genrate_charts()
        #     input("Press Enter to return to the menu...")
        #     clear_console()
        #     return
        
        # elif choice == '2':
        #     genrate_report()
        #     input("Press Enter to return to the menu...")
        #     clear_console()

        #     return
        
        # elif choice == '3':
        #     clear_console()
        #     years = input(("Enter 4 years for back testing (comma separated, e.g. 2008,2009,2020,2021): "))
        #     year_list = [int(year.strip()) for year in years.split(",")]
        #     if len(year_list) != 4:
        #         print("Please enter exactly 4 years.")
        #         input("Press Enter to try again...")
        #         clear_console()
        #         return
        #     clear_console()
        #     back_testing(*year_list)
        #     input("Press Enter to return to the menu...")
        #     clear_console()
        #     return


        
        # elif choice == '4':
        #     print("Exiting the program. Goodbye!")
        #     exit()
       
        # else:
        #     print("Invalid choice. Please enter a number between 1 and 4.")
        #     input("Press Enter to try again...")
        #     clear_console()
        #     return















