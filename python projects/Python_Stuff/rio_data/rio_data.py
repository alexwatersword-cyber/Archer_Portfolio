import pandas as pd
import datetime as DT
import numpy as np
df=pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv')
#this is the top 30 nation by value count of nationality column
print("Top 30 nations by count")
print(df['nationality'].value_counts()[:30])
#calculating the total medals for each nationality
gold = df.groupby('nationality').sum()['gold']
silver = df.groupby('nationality').sum()['silver']
bronze = df.groupby('nationality').sum()['bronze']
total_medals = gold + silver + bronze
print("\nTotal medals by nationality")
print(total_medals)
# Printing USA gold medals count (if present)
if "USA" in gold:
    print(f"\nGold Medals for USA: {gold['USA']}")
else:
    print("\nGold medals for USA not available.")
# handling date of birth and calculating age
now = pd.Timestamp(DT.datetime.now())#convert to todays date to list type format
#handle invalid dates gracefully and date format(e.g., YYYY-MM-DD or MM/DD/YYYY),
df['dob'] = pd.to_datetime(df['dob'], format = '%Y-%m-%d', errors = 'coerce')#convert dob to list type format
#adjust future dates by subtracting 100 years
df['dob'] = df['dob'].apply(lambda x: x - pd.DateOffset(years=100) if x > now else x)
#calculate age in years by dividing the time data by 365.25 days
df['age'] = (now-df['dob']).dt.days // 365.25#calculate age by subtracting dob from todays date and convert to years
print("\nUpdated DataFrame with Age:")
print(df.head())#displays the first few rows
#nation_count = df['nationality'].value_counts()
#print(nation_count)
#gold = df.groupby('nationality').sum()['gold']
#silver = df.groupby('nationality').sum()['silver']
#bronze = df.groupby('nationality').sum()['bronze']
#total_medals = gold + silver + bronze
#print(total_medals)
#print(gold["USA"])

