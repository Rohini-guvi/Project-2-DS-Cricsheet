# Project-2-DS-Cricsheet
Cricsheet - IPL, ODI, T20 and Test Matches Data Analysis 

**Objective:**
The objective of this project is to analyze
-  Team perform across IPL, T20, ODI and Test Matches​
-  Performance of Players across matches​
-  Win/Loss patterns, margins of victory and trends​
-  Present interactive PowerBI dashboards to explore match data​

**Approach:**
- From the website https://cricsheet.org/matches/ , download the match details for IPL, ODI, T20 and Testseries available in JSON format.​
- Using Pandas, Dataframes are created for each match by parsing the JSON files.​
- All the Dataframes are stored in MySQL Database as Tables  for accessing the data using apps like Streamlit and Power BI Desktop.​
- Using Streamlit app, we can view the Tables for IPL, ODI, T20 and Test matches. I have limited the viewing table size as 200000 as the Table size is large.​
- 20 SQL queries are created in Streamlit App to analyze the match data.​
- 10 Visualizations are created in Python to provide match insights.​
- Interactive dashboards are created for each match to analyze Team performance, Players Performance and win/loss patterns
  
**Code flow:**

Streamlit App Page structure

main.py

|---------------ViewTable.Py

|---------------Query.py

**Visualizations:**
- IPL Winning Teams count​
- IPL Matches count held in each locations​
- IPL Matches played over years​
- ODI Matches played by both Male and Female over years​
- Grouped data of Gender, Winner and Event name for ODI matches between teams Australia & India against count​
- T20s matches Target runs against years​
- Performance of MS Dhoni in ODI Matches​
- DB Sharma's wicket count in T20 matches​
- Extra runs added for each Deliveries in DB Sharma's balls​
- Winning Teams played with India across City in Test Matches​
- Chart showing Percent of Toss Winner choosing bat or field Decision​
  
**SQL Queries:**
- Top 10 Batsman in ODIs​
- T20 matches with result as tie​
- IPL Matches with narrow margin of win​
- Top 10 Bowlers in T20s as leading wicket-takers​
- Teams with Highest win percent in Test Cricket​
- IPL Matches with Superover as Target​
- Teams with No.of 6's scored in ODI matches​
- Wickets caught by fielders in Test cricket​
- Teams with No.of 4's scored in T20 matches​
- Batters with No.of 6's scored in IPL matches​
- Count of the Player winning "Player of the match" award in ODIs​
- Teams winning both Toss and Match in T20 matches​
- Batter winning centuries in an inning in Testseries​
- Batter winning centuries in an inning in T20s​
- Batter winning centuries in an inning in ODIs​
- Batter winning centuries in an inning in IPL​
- Batters with No.of 4's scored in Test matches​
- Wickets taken by Bowlers in T20 matches​
- Matches played by Female in ODIs​
- Test Matches with High margin of win​
