import streamlit as st
import functions as f
from data_pipeline import df
def main(df):
    # while True:
    #     f.clear_console()
        st.markdown("Main Menu")
        st.markdown("1. Overview of Economy")
        st.markdown("2. Generate Report")
        st.markdown("3. Rank Economies by Year")
        st.markdown("4. Back Testing")
        st.markdown("5. Compare Countries")
        st.markdown("6. Check Modules")
        st.markdown("7. Exit")

        func_choice = st.text_input("Enter your choice: ")

        if func_choice == "1":
            f.web_choice_1(df)

main(df)

# st.dataframe(df)

