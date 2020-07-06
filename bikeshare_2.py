#librarys

import pandas as pd
from IPython.core.display import Image, display


def main():
    Ciudad=0
    Fecha=0
    month=0
    day=0
    i=0
    while True:
        display(Image('https://gestionhumana8.webnode.es/_files/200000039-2e0842f023/hgushtug%20su.jpg', width=1900, unconfined=True))
        Procesar=input("would like want to see the raw data, answer Yes or Not? ")
        Procesar=Procesar.lower()
        if((Procesar.strip() == 'yes')|(Procesar.strip() == 'not')):
            break
        else: print('Poorly written, write well Yes or Not? ')
        
    if(Procesar=='yes'):
        df1 = pd.read_csv('C:\\Users\\jagorichonp\\Documents\\Udacity\\Proyecto Python\\chicago.csv',sep=',')
        df2= pd.read_csv('C:\\Users\\jagorichonp\\Documents\\Udacity\\Proyecto Python\\new_york_city.csv',sep=',')
        df3 = pd.read_csv('C:\\Users\\jagorichonp\\Documents\\Udacity\\Proyecto Python\\washington.csv',sep=',')
        df=pd.concat([df1,df2],axis=0)
        df=pd.concat([df,df3],axis=0)
        print(df[i:i+5])
        while True:
            F=input("they would like to see 5 more rows of the data?, answer Yes or Not ")
            F=F.lower()
            if((F.strip() == 'yes')|(F.strip() == 'not')):
                if(F=='yes'):
                    i=i+5
                    print(df[i:i+5])
                else: break
            else: print('Poorly written, write well Yes or Not? ')
                
    if(Procesar=='not'):
        while True:
            Ciudad = input("Would you like to see data for Chicago, New York, or Washington?")
            Ciudad=Ciudad.lower()
            if((Ciudad.strip() == 'new york')|(Ciudad.strip() == 'washington')|(Ciudad.strip() == 'chicago')):
                if (Ciudad.strip() == 'new york'):
                    display(Image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/I_Love_New_York.svg/800px-I_Love_New_York.svg.png', width=1900, unconfined=True))
                    while True:
                        Fecha = input("Would you like to filter the data by month, day, or not at all?")
                        Fecha=Fecha.lower()
                        if((Fecha.strip() == 'month')|(Fecha.strip() == 'day')|(Fecha.strip() == 'not')):
                            if(Fecha.strip() == 'month'):
                                while True:
                                    month = input("Which month - January, February, March, April, May, or June?")
                                    month=month.lower()
                                    if((month.strip() == 'january')|(month.strip() == 'february')|(month.strip() == 'march')|(month.strip() == 'april')|(month.strip() == 'may')|(month.strip() == 'june')):
                                        break
                                    else: print('Poorly written, write well Junuary, Febraury, March, April, May, June')
                                break
                            if(Fecha.strip() == 'day'):
                                while True:
                                    day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
                                    day=day.lower()
                                    if((day.strip() == 'monday')|(day.strip() == 'tuesday')|(day.strip() == 'wednesday')|(day.strip() == 'thursday')|(day.strip() == 'friday')|(day.strip() == 'saturday')|(day.strip() == 'sunday')):
                                        break
                                    else: print('Poorly written, write well Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday')
                                break
                            if(Fecha.strip() == 'not'):
                                break
                        else: print('Poorly written, write well month, day or not')            
                    break
                if(Ciudad.strip() == 'washington'):
                    display(Image('https://img.lovepik.com/element/40157/1769.png_1200.png', width=1900, unconfined=True))
                    while True:
                        Fecha = input("Would you like to filter the data by month, day, or not at all?")
                        Fecha=Fecha.lower()
                        if((Fecha.strip() == 'month')|(Fecha.strip() == 'day')|(Fecha.strip() == 'not')):
                            if(Fecha.strip() == 'month'):
                                while True:
                                    month = input("Which month - January, February, March, April, May, or June?")
                                    month=month.lower()
                                    if((month.strip() == 'january')|(month.strip() == 'february')|(month.strip() == 'march')|(month.strip() == 'april')|(month.strip() == 'may')|(month.strip() == 'june')):
                                        break
                                    else: print('Poorly written, write well Junuary, Febraury, March, April, May, June')
                                break
                            if(Fecha.strip() == 'day'):
                                while True:
                                    day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
                                    day=day.lower()
                                    if((day.strip() == 'monday')|(day.strip() == 'tuesday')|(day.strip() == 'wednesday')|(day.strip() == 'thursday')|(day.strip() == 'friday')|(day.strip() == 'saturday')|(day.strip() == 'sunday')):
                                        break
                                    else: print('Poorly written, write well Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday')
                                break
                            if(Fecha.strip() == 'not'):
                                break
                        else: print('Poorly written, write well month, day or not')            
                    break
                if(Ciudad.strip() == 'chicago'):
                    display(Image('https://a.espncdn.com/i/teamlogos/nba/500/chi.png', width=1900, unconfined=True))
                    while True:
                        Fecha = input("Would you like to filter the data by month, day, or not at all?")
                        Fecha=Fecha.lower()
                        if((Fecha.strip() == 'month')|(Fecha.strip() == 'day')|(Fecha.strip() == 'not')):
                            if(Fecha.strip() == 'month'):
                                while True:
                                    month = input("Which month - January, February, March, April, May, or June?")
                                    month=month.lower()
                                    if((month.strip() == 'january')|(month.strip() == 'february')|(month.strip() == 'march')|(month.strip() == 'april')|(month.strip() == 'may')|(month.strip() == 'june')):
                                        break
                                    else: print('Poorly written, write well Junuary, Febraury, March, April, May, June')
                                break
                            if(Fecha.strip() == 'day'):
                                while True:
                                    day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
                                    day=day.lower()
                                    if((day.strip() == 'monday')|(day.strip() == 'tuesday')|(day.strip() == 'wednesday')|(day.strip() == 'thursday')|(day.strip() == 'friday')|(day.strip() == 'saturday')|(day.strip() == 'sunday')):
                                        break
                                    else: print('Poorly written, write well Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday')
                                break
                            if(Fecha.strip() == 'not'):
                                break
                        else: print('Poorly written, write well month, day or not')     
                    break
            else: print('Poorly written, write well name of the city')

        if(Ciudad=='chicago'):
            df = pd.read_csv('C:\\Users\\jagorichonp\\Documents\\Udacity\\Proyecto Python\\chicago.csv',sep=',')
        if(Ciudad=='new york'):
            df = pd.read_csv('C:\\Users\\jagorichonp\\Documents\\Udacity\\Proyecto Python\\new_york_city.csv',sep=',')
        if(Ciudad=='washington'):
            df = pd.read_csv('C:\\Users\\jagorichonp\\Documents\\Udacity\\Proyecto Python\\washington.csv',sep=',')
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['Month_Start'] =df['Start Time'].dt.strftime('%B')
        df['Day_Start'] =df['Start Time'].dt.strftime('%A')
        df['hour_Start'] =df['Start Time'].dt.hour
        df['Month_Start']=df['Month_Start'].str.lower()
        df['Day_Start']=df['Day_Start'].str.lower()
        if(Fecha=='month'):
            df = df[df['Month_Start']== month]
    
            popular_month = df['Month_Start'].mode()[0]
            print('Popular month: '+popular_month)
    
            popular_day = df['Day_Start'].mode()[0]
            print('Popular day: '+popular_day)
    
            popular_hour = df['hour_Start'].mode()[0]
            print('Popular hour: ',popular_hour)
    
            Popular_Starion_Start=df['Start Station'].mode()[0]
            print('Popular_Station_Start: '+Popular_Starion_Start)
        
            Popular_Station_End=df['End Station'].mode()[0]
            print('Popular_Station_End: '+Popular_Station_End)
    
            df['Start-End Station']=df['Start Station']+"-"+df['End Station']
            Popular_Station_Star_End=df['Start-End Station'].mode()[0]
            print('Popular_Station_Star_End: '+Popular_Station_Star_End)
    
            Total_time_travel=df['Trip Duration'].sum()
            print('Total_time_travel: ',Total_time_travel,' min')
    
            Average_travel=df['Trip Duration'].mean()
            print('Average_travel: ',Average_travel)
    
            user_types = df['User Type'].value_counts()
            print('user_types: ',user_types)
        if(Fecha=='day'):
            df = df[df['Day_Start']== day]
            popular_month = df['Month_Start'].mode()[0]
            print('Popular month: '+popular_month)
    
            popular_day = df['Day_Start'].mode()[0]
            print('Popular day: '+popular_day)
    
            popular_hour = df['hour_Start'].mode()[0]
            print('Popular hour: ',popular_hour)
    
            Popular_Starion_Start=df['Start Station'].mode()[0]
            print('Popular_Station_Start: '+Popular_Starion_Start)
        
            Popular_Station_End=df['End Station'].mode()[0]
            print('Popular_Station_End: '+Popular_Station_End)
        
            df['Start-End Station']=df['Start Station']+"-"+df['End Station']
            Popular_Station_Star_End=df['Start-End Station'].mode()[0]
            print('Popular_Station_Star_End: '+Popular_Station_Star_End)
        
            Total_time_travel=df['Trip Duration'].sum()
            print('Total_time_travel: ',Total_time_travel,' min')
    
            Average_travel=df['Trip Duration'].mean()
            print('Average_travel: ',Average_travel)
    
            user_types = df['User Type'].value_counts()
            print('user_types: ',user_types)
        if(Fecha=='not'):
            popular_month = df['Month_Start'].mode()[0]
            print('Popular month: '+popular_month)
        
            popular_day = df['Day_Start'].mode()[0]
            print('Popular day: '+popular_day)
    
            popular_hour = df['hour_Start'].mode()[0]
            print('Popular hour: ',popular_hour)
    
            Popular_Starion_Start=df['Start Station'].mode()[0]
            print('Popular_Station_Start: '+Popular_Starion_Start)
        
            Popular_Station_End=df['End Station'].mode()[0]
            print('Popular_Station_End: '+Popular_Station_End)
    
            df['Start-End Station']=df['Start Station']+"-"+df['End Station']
            Popular_Station_Star_End=df['Start-End Station'].mode()[0]
            print('Popular_Station_Star_End: '+Popular_Station_Star_End)
    
            Total_time_travel=df['Trip Duration'].sum()
            print('Total_time_travel: ',Total_time_travel,' min')
    
            Average_travel=df['Trip Duration'].mean()
            print('Average_travel: ',Average_travel)
    
            user_types = df['User Type'].value_counts()
            print('user_types: ',user_types)
            
        if((Ciudad=='chicago')|(Ciudad=='new york')):
            Gender_types = df['Gender'].value_counts()
            print('Gender_types: ', Gender_types)
        
            Year_recent=df['Birth Year'].min()
            print('Year_recent: ',Year_recent)
        
            Year_Common=df['Birth Year'].mode()[0]
            print('Year_Common: ',Year_Common)
                    
    display(Image('https://i.pinimg.com/236x/87/6a/af/876aaf61b09aa2617a93cd79af4a49c1.jpg', width=1900, unconfined=True))        
if __name__== "__main__":
    main()