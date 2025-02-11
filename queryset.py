import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

class SQLQuerySet:
    def __init__(self):
        self.db=create_engine('mysql+pymysql://USER:root@localhost:3306/cricsheet')

    def execute_query(self,query):
        #Execute the query and Display the out table as Dataframe
        try:
            data=pd.read_sql(query,self.db)
            st.dataframe(data)
        except Exception as e:
            st.error(str(e))
        return
    
    #Query-1:Top 10 Batsman in ODIs
    def query1(self):
        query="""select Batter,sum(Batter_Runs_per_over) as "Total_Runs" from cricsheet.odis
        group by Batter
        order by sum(Total_Runs_per_over)  DESC
        LIMIT 10;"""
        self.execute_query(query)
        return
    
    #Query-2:T20 matches with result as tie
    def query2(self):
        query="""select * from cricsheet.t20s where Result='tie';"""
        self.execute_query(query)
        return
    
    #Query-3:IPL Matches with narrow margin of win like win by less than 2 wickets or less than 10 runs
    def query3(self):
        query="""select * from cricsheet.ipl
        where Winby='runs' and Winby_value<=10
        or Winby='wickets' and Winby_value<=2;"""
        self.execute_query(query)
        return
    
    #Query-4:Top 10 Bowlers in T20s as leading wicket-takers
    def query4(self):
        query="""SELECT Bowler,count(Wicket_Kind) from cricsheet.t20s
        group by Bowler
        order by count(Wicket_Kind) DESC
        LIMIT 10;"""
        self.execute_query(query)
        return
    
    #Query-5:Teams with Highest win percent in Test Cricket
    def query5(self):
        query="""select Batting_team,
        count(Batting_team) as "Total_Matches_Played",
        count(Winner) as "Winning_match_count",
        count(Result) as "Draw_match_count",
        ((count(Winner)+0.5*count(Result))/count(Batting_team))*100 as "Winning_percent" from cricsheet.testseries
        group by Batting_team
        order by Winning_percent DESC;"""
        self.execute_query(query)
        return
    
    #Query-6:IPL Matches with Superover as Target
    def query6(self):
        query="""select * from cricsheet.ipl where Target_SuperOver='Super_over';"""
        self.execute_query(query)
        return
    
    #Query-7:Teams with No.of 6's scored in ODI matches
    def query7(self):
        query="""select Batting_Team,count(Total_Runs_per_over) as "No_of_Sixes_scored" from cricsheet.odis
        where Total_Runs_per_over=6
        group by Batting_Team
        order by No_of_Sixes_scored DESC;"""
        self.execute_query(query)
        return
    
    #Query-8:Wickets caught by fielders in Test cricket
    def query8(self):
        query="""select Bowler,Wicket_Kind,Wicket_Player_out,Wicket_fielders from cricsheet.testseries
        where Wicket_fielders is not null;"""
        self.execute_query(query)
        return
    
    #Query-9:Teams with No.of 4's scored in T20 matches
    def query9(self):
        query="""select Batting_Team,count(Total_Runs_per_over) as "No_of_4s_scored" from cricsheet.t20s
        where Total_Runs_per_over=4
        group by Batting_Team
        order by No_of_4s_scored DESC;"""
        self.execute_query(query)
        return
    
    #Query-10:Batters with No.of 6's scored in IPL matches
    def query10(self):
        query="""select Batter,count(Batter_Runs_per_over=6) as "No_of_Sixes_scored" from cricsheet.ipl
        group by Batter
        order by No_of_Sixes_scored DESC;"""
        self.execute_query(query)
        return
    
    #Query-11:Count of the Player winning "Player of the match" award in ODIs
    def query11(self):
        query="""select DISTINCT season,Player_of_match,count(Player_of_match)as "Count" from cricsheet.odis
        group by season,Player_of_match,Innings_Over
        order by count(Player_of_match) DESC;"""
        self.execute_query(query)
        return
    
    #Query-12:Teams winning both Toss and Match in T20 matches
    def query12(self):
        query="""select season,Teams,Winner,Toss_Winner,Toss_Decision from cricsheet.t20s
        where Toss_Winner=Winner
        group by season,Teams,Winner,Toss_Winner,Toss_Decision;"""
        self.execute_query(query)
        return
    
    #Query-13:Batter winning centuries in an inning in Testseries
    def query13(self):
        query="""select Batting_Team,Batter,sum(Batter_Runs_per_over) as "Total_run_in_a_Inning" from cricsheet.testseries
        group by Batting_Team,Batter,Innings_Over
        having Total_run_in_a_Inning>=100
        order by Total_run_in_a_Inning DESC;"""
        self.execute_query(query)
        return
    
    #Query-14:Batter winning centuries in an inning in T20s
    def query14(self):
        query="""select Batting_Team,Batter,sum(Batter_Runs_per_over) as "Total_run_in_a_Inning" from cricsheet.t20s
        group by Batting_Team,Batter,Innings_Over
        having Total_run_in_a_Inning>=100
        order by Total_run_in_a_Inning DESC;"""
        self.execute_query(query)
        return
    
    #Query-15:Batter winning centuries in an inning in ODIs
    def query15(self):
        query="""select Batting_Team,Batter,sum(Batter_Runs_per_over) as "Total_run_in_a_Inning" from cricsheet.odis
        group by Batting_Team,Batter,Innings_Over
        having Total_run_in_a_Inning>=100
        order by Total_run_in_a_Inning DESC;"""
        self.execute_query(query)
        return
    
    #Query-16:Batter winning centuries in an inning in IPL
    def query16(self):
        query="""select Batting_Team,Batter,sum(Batter_Runs_per_over) as "Total_run_in_a_Inning" from cricsheet.ipl
        group by Batting_Team,Batter,Innings_Over
        having Total_run_in_a_Inning>=100
        order by Total_run_in_a_Inning DESC;"""
        self.execute_query(query)
        return
    
    #Query-17:Batters with No.of 4's scored in Test matches
    def query17(self):
        query="""select Batter,count(Batter_Runs_per_over=4) as "No_of_4s_scored" from cricsheet.testseries
        group by Batter
        order by No_of_4s_scored DESC;"""
        self.execute_query(query)
        return
        
    #Query-18:Wickets taken by Bowlers in T20 matches
    def query18(self):
        query="""select Bowler,Wicket_Kind,Wicket_Player_out from cricsheet.t20s
        where Wicket_fielders is null and Wicket_Kind is not null
        LIMIT 20000;"""
        self.execute_query(query)
        return
    
    #Query-19:Matches played by Female in ODIs
    def query19(self):
        query="""select * from cricsheet.odis where Gender='female'
        LIMIT 200000;"""
        self.execute_query(query)
        return
    
    #Query-20:Test Matches with High margin of win like win by greater than 10 wickets or greater than 200 runs
    def query20(self):
        query="""select * from cricsheet.testseries
        where Winby='runs' and Winby_value>=200
        or Winby='wickets' and Winby_value>=10
        LIMIT 200000;"""
        self.execute_query(query)
        return