import os
import re
import json
import pandas as pd
from sqlalchemy import create_engine

class TableCreation:
    def __init__(self):
        self.db=create_engine('mysql+pymysql://USER:root@localhost:3306/cricsheet')

    # Fetching info and innings details from each file and converting into Dataframe
    def match_dataframe(self,path,file_name):
        #Create empty dataframe for concatenation of data
        info_data1=pd.DataFrame()
        info_data2=pd.DataFrame()
        info_data3=pd.DataFrame()
        info_data4=pd.DataFrame()
        info_data5=pd.DataFrame()
        info_data6=pd.DataFrame()
        info_data7=pd.DataFrame()
        info_data8=pd.DataFrame()
        info_data9=pd.DataFrame()
        info_data10=pd.DataFrame()
        info_data11=pd.DataFrame()
        info_data12=pd.DataFrame()
        info_data13=pd.DataFrame()
        info_data14=pd.DataFrame()
        info_data15=pd.DataFrame()
        info_data16=pd.DataFrame()

        # Get the list of all files in the directory
        files = os.listdir(path)
            
        #filtering only the files with .json ext
        files_json = [i for i in files if re.findall("[0-9].json",i)]

        for file in files_json:
            print(file)
            filepath=path+file
            file_content= json.load(open(filepath,'r'))

            if 'officials' in file_content['info'].keys():
                Match_referees= [file_content['info']['officials']['match_referees'][0] if 'match_referees' in file_content['info']['officials'].keys() else None]
                Reserve_umpires= [file_content['info']['officials']['reserve_umpires'][0] if 'reserve_umpires' in file_content['info']['officials'].keys() else None]
                Tv_umpires= [file_content['info']['officials']['tv_umpires'][0] if 'tv_umpires' in file_content['info']['officials'].keys() else None]
                Official_umpires= [file_content['info']['officials']['umpires'] if 'umpires' in file_content['info']['officials'].keys() else None]
            else:
                Official_umpires= None
                Tv_umpires=None
                Reserve_umpires=None
                Match_referees=None

            for inn in range(len(file_content['innings'])):
                for over in range(len(file_content['innings'][inn]['overs'])):
                    for delivery in range(len(file_content['innings'][inn]['overs'][over]['deliveries'])):
                        
                        if 'wickets' in file_content['innings'][inn]['overs'][over]['deliveries'][delivery].keys():
                            if 'fielders' in file_content['innings'][inn]['overs'][over]['deliveries'][delivery]['wickets'][0].keys():
                                fielders=[file_content['innings'][inn]['overs'][over]['deliveries'][delivery]['wickets'][0]['fielders'][0]]
                            else:
                                fielders=None
                        else:
                            fielders=None

                        win_key=[''.join(file_content['info']['outcome']['by'].keys()) if 'by' in file_content['info']['outcome'].keys() else None]
                        
                        data=pd.DataFrame(
                            {
                                "Balls_per_over" : [file_content['info']['balls_per_over'] if 'balls_per_over' in file_content['info'].keys() else None],
                                "City" : [file_content['info']['city'] if 'city' in file_content['info'].keys() else None],
                                "Dates" : [file_content['info']['dates'] if 'dates' in file_content['info'].keys() else None],
                                "season" : [file_content['info']['season'] if 'season' in file_content['info'].keys() else None],
                                "Event_Name" : [file_content['info']['event']['name'] if 'event' in file_content['info'].keys() else None],
                                "Overs" : [file_content['info']['overs'] if 'overs' in file_content['info'].keys() else None],
                                "Gender" : [file_content['info']['gender'] if 'gender' in file_content['info'].keys() else None],
                                "Match_type" : [file_content['info']['match_type'] if 'match_type' in file_content['info'].keys() else None],
                                "Match_referees" : Match_referees,
                                "Reserve_umpires" : Reserve_umpires,
                                "Tv_umpires" : Tv_umpires,
                                "Official_umpires" : Official_umpires,
                                "Winner" : [file_content['info']['outcome']['winner'] if 'winner' in file_content['info']['outcome'].keys() else None],
                                "Eliminator": [file_content['info']['outcome']['eliminator'] if 'eliminator' in file_content['info']['outcome'].keys() else None],
                                "Winby" : win_key,
                                "Winby_value" : [file_content['info']['outcome']['by'].get(win_key[0]) if 'by' in file_content['info']['outcome'].keys() else None],
                                "Result" : [file_content['info']['outcome']['result'] if 'result' in file_content['info']['outcome'].keys() else None],
                                "Player_of_match" : [file_content['info']['player_of_match'] if 'player_of_match' in file_content['info'].keys() else None],
                                "Teams" : [file_content['info']['teams'] if 'teams' in file_content['info'].keys() else None],
                                "Team_type" : [file_content['info']['team_type'] if 'team_type' in file_content['info'].keys() else None],
                                "Players" : [file_content['info']['players'] if 'players' in file_content['info'].keys() else None],
                                "Toss_Winner" : [file_content['info']['toss']['winner'] if 'winner' in file_content['info']['toss'].keys() else None],
                                "Toss_Decision" : [file_content['info']['toss']['decision'] if 'decision' in file_content['info']['toss'].keys() else None],
                                "Venue" : [file_content['info']['venue'] if 'venue' in file_content['info'].keys() else None],
                                "Batting_Team" : file_content['innings'][inn]['team'],
                                "Innings_Over" : over+1,
                                "Deliveries" : delivery+1,
                                "Batter" : file_content['innings'][inn]['overs'][over]['deliveries'][delivery]['batter'],
                                "Bowler" : file_content['innings'][inn]['overs'][over]['deliveries'][delivery]['bowler'],
                                "Non-Striker" : file_content['innings'][inn]['overs'][over]['deliveries'][delivery]['non_striker'],
                                "Batter_Runs_per_over" : [file_content['innings'][inn]['overs'][over]['deliveries'][delivery]['runs']['batter']],
                                "Extras_per_over" : [file_content['innings'][inn]['overs'][over]['deliveries'][delivery]['runs']['extras']],
                                "Total_Runs_per_over" : [file_content['innings'][inn]['overs'][over]['deliveries'][delivery]['runs']['total']],
                                "Wicket_Kind" : [file_content['innings'][inn]['overs'][over]['deliveries'][delivery]['wickets'][0]['kind'] if 'wickets' in file_content['innings'][inn]['overs'][over]['deliveries'][delivery].keys() else None],
                                "Wicket_Player_out" : [file_content['innings'][inn]['overs'][over]['deliveries'][delivery]['wickets'][0]['player_out'] if 'wickets' in file_content['innings'][inn]['overs'][over]['deliveries'][delivery].keys() else None],
                                "Wicket_fielders" : fielders,
                                "Powerplays" : [file_content['innings'][inn]['powerplays'] if 'powerplays' in file_content['innings'][inn].keys() else None],
                                "Target_SuperOver" : [file_content['innings'][len(file_content['innings'])-1]['target']['runs'] if 'target' in file_content['innings'][len(file_content['innings'])-1].keys() else 'Super_over']
                            })
                        
                        a=pd.to_datetime(file_content['info']['dates'][0])
                        season=int(a.strftime('%Y'))
                        if 2000<= season and season<= 2005:
                            info_data1 = pd.concat([info_data1,data])
                        elif 2006<= season and season<= 2010:
                            info_data15 = pd.concat([info_data15,data])
                        elif season== 2011:
                            info_data16 = pd.concat([info_data16,data])
                        elif season==2012:
                            info_data2 = pd.concat([info_data2,data])
                        elif season==2013:
                            info_data3 = pd.concat([info_data3,data])
                        elif season==2014:
                            info_data4 = pd.concat([info_data4,data])
                        elif season==2015:
                            info_data5 = pd.concat([info_data5,data])
                        elif season==2016:
                            info_data6 = pd.concat([info_data6,data])
                        elif season==2017:
                            info_data7 = pd.concat([info_data7,data])
                        elif season==2018:
                            info_data8 = pd.concat([info_data8,data])
                        elif season==2019:
                            info_data9 = pd.concat([info_data9,data])
                        elif season==2020:
                            info_data10 = pd.concat([info_data10,data])
                        elif season==2021:
                            info_data11 = pd.concat([info_data11,data])
                        elif season==2022:
                            info_data12 = pd.concat([info_data12,data])
                        elif season==2023:
                            info_data13 = pd.concat([info_data13,data])
                        else:
                            info_data14 = pd.concat([info_data14,data])
        
        #Concatenation of all Dataframes
        df=pd.concat([info_data1,info_data2,info_data3,info_data4,info_data5,info_data6,
                      info_data7,info_data8,info_data9,info_data10,info_data11,info_data12,
                      info_data13,info_data14,info_data15,info_data16],ignore_index=True)
                        
        # Dumping Dataframe into CSV File
        df.to_csv(f"{file_name}.csv")
        
        #Read the CSV files and store the values in SQL Database
        df1=pd.read_csv(f"{file_name}.csv",index_col=0,low_memory=False)
        df1.to_sql(name=f"{file_name}",con=self.db)
        
        return
    
        