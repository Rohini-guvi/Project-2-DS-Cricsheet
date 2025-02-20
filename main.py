from readdata import TableCreation
import streamlit as st

st.title("Cricsheet Match Data Analysis ")

tc = TableCreation()

# Calling Match_Dataframe function to Create tables for IPL,ODIs,Test Series and T20s
tc.match_dataframe('C:/Users/HP/OneDrive/Project2-Cricsheet/ipl_json/','ipl')
tc.match_dataframe('C:/Users/HP/OneDrive/Project2-Cricsheet/odis_json/','odis')
tc.match_dataframe('C:/Users/HP/OneDrive/Project2-Cricsheet/t20s_json/','t20s')
tc.match_dataframe('C:/Users/HP/OneDrive/Project2-Cricsheet/tests_json/','testseries')

current_page=st.navigation([st.Page("ViewTable.py"),
                            st.Page("Query.py")])

current_page.run()