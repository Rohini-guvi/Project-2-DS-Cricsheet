import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

#View existing tables
st.write("View Databases for IPL,T20s,TestSeries,ODIs")

class SQLTableDisplay:
    def __init__(self):
        self.db=create_engine('mysql+pymysql://USER:root@localhost:3306/cricsheet')

    #Function to read SQL tables and display the table
    def Table_Display(self,tablename):
        query=f"SELECT * FROM {tablename} LIMIT 200000"
        data=pd.read_sql(query,self.db)
        st.dataframe(data)
        return

td = SQLTableDisplay()

#Select the Database to be viewed
option = st.selectbox(
    "Select the Database to be viewed",
    ("IPL DataBase","ODI DataBase","T20s DataBase","TestSeries DataBase")
)

if option=="IPL DataBase":
    td.Table_Display("ipl")  
elif option=="ODI DataBase":
    td.Table_Display("odis")
elif option=="T20s DataBase":
    td.Table_Display("t20s")
else:
    td.Table_Display("testseries")