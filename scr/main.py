from menu_manager import menu


if __name__ == "__main__":  
    while True:
        try:
            menu()
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to return to the menu...")