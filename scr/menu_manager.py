from report_genrator import  genrate_report,over_view_of_economy_chart

from functions import choice_1 ,choice_2,choice_3 ,compare_countries,df
 










def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')



def start_menu():

            clear_console()
            print("Main Menu")
            print("1. over view of economy ")
            print("2. Generate Report")
            print("3. Back Testing")
            print("4. Compare Countries") 
            print("5. check modules")
            print("6. Exit")
            
            func_choice = input("Enter your choice: ")
           
            if func_choice == "1":
                    choice_1()
 
            elif func_choice == "2":
                    choice_2()

            elif func_choice == '3':
                    choice_3()
                    
                    
           
            elif func_choice == '4':
                    clear_console()
                    country1 = input("Enter the first country (default: India): ")
                    country2 = input("Enter the second country (default: USA): ")
                    country3 = input("Enter the third country (default: China): ")
                    year = int(input("Enter the year for comparison (default: 2020): "))
                    
                    if not country1:
                        country1 = "India"
                    if not country2:
                        country2 = "USA"
                    if not country3:
                        country3 = "China"
                    if not year:
                        year = 2020
                    
                    compare_countries(country1=country1, country2=country2, country3=country3, year=year)
                    input("Press Enter to return to the menu...")
                    clear_console()
           
            else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
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















