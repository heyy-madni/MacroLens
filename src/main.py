#main.py

from menu_manager import main
from data_pipeline import df

#todo add multi country in Regime Periods & Condition Checker
#todo use income per capita 
#todo refactor menu and add library

if __name__ == "__main__":  
    while True:
        try:
            main(df) 
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to return to the menu...")