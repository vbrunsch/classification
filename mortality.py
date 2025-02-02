
'''
new deaths
https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_deaths.csv

excess mortality + population
https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv

global mortality
https://raw.githubusercontent.com/akarlinsky/world_mortality/main/world_mortality.csv
country_name,year,time,time_unit,deaths
https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_deaths_usafacts.csv

https://data.cdc.gov/api/views/xkkf-xrst/rows.csv
'''
country="Ireland"
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("https://raw.githubusercontent.com/akarlinsky/world_mortality/main/world_mortality.csv")
print(data.columns)
d3=data[data["country_name"]==country].fillna(0)
d3=d3#[d3["year"].astype(int)>2019]
d3.to_csv(country+"_mortality1.csv")
#d3["deaths"]=d3["deaths"]
d3['year']=d3['year']#[str(x) for x in pd.DatetimeIndex(d3['date']).year.to_list()]
#d3["Date"]=d3['time']#pd.to_datetime(d3['date']).dt.strftime('%W')# - pd.to_timedelta(7, unit='d')                                                                                           
d3["Date"]=d3["year"].apply(str)+"_"+d3["time"].apply(str)
d3['Date'] = pd.Categorical(d3['Date'], ['2015_1', '2015_2', '2015_3', '2015_4', '2015_5', '2015_6', '2015_7', '2015_8', '2015_9','2015_10', '2015_11', '2015_12', '2016_1', '2016_2', '2016_3', '2016_4', '2016_5', '2016_6', '2016_7', '2016_8', '2016_9', '2016_10', '2016_11', '2016_12','2017_1', '2017_2', '2017_3', '2017_4', '2017_5', '2017_6', '2017_7', '2017_8', '2017_9', '2017_10', '2017_11', '2017_12','2018_1', '2018_2', '2018_3', '2018_4', '2018_5', '2018_6', '2018_7', '2018_8', '2018_9', '2018_10', '2018_11', '2018_12','2019_1', '2019_2', '2019_3', '2019_4', '2019_5', '2019_6', '2019_7', '2019_8', '2019_9', '2019_10', '2019_11', '2019_12','2020_1',  '2020_2', '2020_3', '2020_4', '2020_5', '2020_6', '2020_7', '2020_8', '2020_9', '2020_10', '2020_11', '2020_12','2021_1', '2021_2', '2021_3', '2021_4', '2021_5', '2021_6'])
print(d3["Date"])
df0=d3.sort_values('Date')#.groupby(['Date'])["deaths"].sum().reset_index().sort_values('Date')

x=df0["Date"].to_list()
#[str(x) for x in df0["Date"].to_list()]
print(x)
y=df0["deaths"].to_list()
'''
x=range(0,len(d3))
y=[z for z in d3["new_deaths"].to_list()]
print(y)
'''
fig, ax = plt.subplots()
plt.xticks(rotation=70)
#x=[str(x) for x in df0["Date"].to_list()]
#plt.plot(x,y,label='All deaths')

plt.plot(range(0,12),y[:12],label='2015')
plt.plot(range(0,12),y[12:24],label='2016')
plt.plot(range(0,12),y[24:36],label='2017')
plt.plot(range(0,12),y[36:48],label='2018')
plt.plot(range(0,12),y[48:60],label='2019')
plt.plot(range(0,12),y[60:72],label='2020')
#print(sum(y[60:72]))
plt.plot(range(0,6),y[72:78],label='2021')
#print(y[:12],y[72:])

plt.title(country+" (grouped by months)")
#plt.locator_params(axis='x', nbins=20)
#fig, ax = plt.subplots()
#print(x)
#plt.plot(...)
#print(ax.xaxis.get_ticklabels())
every_nth = 1
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
#plt.show()



data2=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_deaths.csv").fillna(0)
#x1=range(0,len(data2["date"]))
#y1=data2["Ireland"].to_list()

d4=data2[["date",country]]
d4['year']=[str(x) for x in pd.DatetimeIndex(d4['date']).year.to_list()]
d4['month']=[str(x) for x in pd.DatetimeIndex(d4['date']).month.to_list()]
#d4["Date"]=pd.to_datetime(d4['date']).dt.strftime('%M')# - pd.to_timedelta(7, unit='d')
d4["Date"]=d4["year"]+"_"+d4["month"]
d4['Date'] = pd.Categorical(d4['Date'], ['2020_1', '2020_2', '2020_3', '2020_4', '2020_5', '2020_6', '2020_7', '2020_8', '2020_9','2020_10', '2020_11', '2020_12', '2021_1', '2021_2', '2021_3', '2021_4', '2021_5', '2021_6', '2021_7', '2021_8', '2021_9','2021_10'])
#print(d4["Date"])

d5=d4[["Date",country]]
#print(d5)
#print(pd.DatetimeIndex(d4['date']).year.to_list())
#d4['Date'] = pd.to_datetime(d4['date']) - pd.to_timedelta(7, unit='d')
df = d5.groupby(['Date'])[country].sum().reset_index().sort_values('Date')
print(df)
df.drop([21])
print(df)
x1=[str(x) for x in df["Date"].to_list()]
print(x1)
y1=df[country].to_list()
print(y1)
print(x)
print(y)
import seaborn as sns
'''
#plt.plot(x1,y1)
#plt.xticks(x1,y1)
#locs, labels = plt.xticks()
#plt.setp(labels, rotation=90)
'''
#plt.xticks(rotation=70)
plt.plot(x1, y1,label='Deaths from COVID-19')
#plt.title(country)
#plt.xticks(x1,y1)                                                                                                                                                                  plt.xticks(rotation=70) 
#locs, labels = plt.xticks()

every_nth = 10
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)  
#plt.setp(labels, rotation=90)

plt.legend()
plt.show()
