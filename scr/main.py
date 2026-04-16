from menu_manager import menu



#todo add multi country in Regime Periods & Condition Checker


if __name__ == "__main__":  
    while True:
        try:
            menu() 
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to return to the menu...")