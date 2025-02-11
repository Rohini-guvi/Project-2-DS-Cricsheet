import streamlit as st
from queryset import SQLQuerySet

st.header("Query to get Match Insights")

# Initialize Query Function
sql_query = SQLQuerySet()

operation = st.selectbox("Select a Query",["Top 10 Batsman in ODIs",
                                                   "T20 matches with result as tie",
                                                   "IPL Matches with narrow margin of win",
                                                   "Top 10 Bowlers in T20s as leading wicket-takers",
                                                   "Teams with Highest win percent in Test Cricket",
                                                   "IPL Matches with Superover as Target",
                                                   "Teams with No.of 6's scored in ODI matches",
                                                   "Wickets caught by fielders in Test cricket",
                                                   "Teams with No.of 4's scored in T20 matches",
                                                   "Batters with No.of 6's scored in IPL matches",
                                                   """Count of the Player winning "Player of the match" award in ODIs""",
                                                   "Teams winning both Toss and Match in T20 matches",
                                                   "Batter winning centuries in an inning in Testseries",
                                                   "Batter winning centuries in an inning in T20s",
                                                   "Batter winning centuries in an inning in ODIs",
                                                   "Batter winning centuries in an inning in IPL",
                                                   "Batters with No.of 4's scored in Test matches",
                                                   "Wickets taken by Bowlers in T20 matches",
                                                   "Matches played by Female in ODIs",
                                                   "Test Matches with High margin of win"
                                                   ])

if operation=="Top 10 Batsman in ODIs":
    sql_query.query1()
elif operation=="T20 matches with result as tie":
    sql_query.query2()
elif operation=="IPL Matches with narrow margin of win":
    sql_query.query3()
elif operation=="Top 10 Bowlers in T20s as leading wicket-takers":
    sql_query.query4()
elif operation== "Teams with Highest win percent in Test Cricket":
    sql_query.query5()
elif operation=="IPL Matches with Superover as Target":
    sql_query.query6()
elif operation=="Teams with No.of 6's scored in ODI matches":
    sql_query.query7()
elif operation=="Wickets caught by fielders in Test cricket":
    sql_query.query8()
elif operation=="Teams with No.of 4's scored in T20 matches":
    sql_query.query9()
elif operation=="Batters with No.of 6's scored in IPL matches":
    sql_query.query10()
elif operation=="""Count of the Player winning "Player of the match" award in ODIs""":
    sql_query.query11()
elif operation=="Teams winning both Toss and Match in T20 matches":
    sql_query.query12()
elif operation=="Batter winning centuries in an inning in Testseries":
    sql_query.query13()
elif operation=="Batter winning centuries in an inning in T20s":
    sql_query.query14()
elif operation=="Batter winning centuries in an inning in ODIs":
    sql_query.query15()
elif operation=="Batter winning centuries in an inning in IPL":
    sql_query.query16()
elif operation=="Batters with No.of 4's scored in Test matches":
    sql_query.query17()
elif operation=="Wickets taken by Bowlers in T20 matches":
    sql_query.query18()
elif operation=="Matches played by Female in ODIs":
    sql_query.query19()
else:
    sql_query.query20()