
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
import datetime
from dateutil.relativedelta import relativedelta
country="Finland"
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
dd1=[]
ind=0
for el in d3['time'].to_list():
    dd1.append(datetime.date(d3["year"].to_list()[ind], 1, 1) + relativedelta(weeks=+el))
    ind+=1
d3["Date1"]=[str(x) for x in pd.DatetimeIndex(dd1).month.to_list()]
#[datetime.date(d3["year"], 1, 1) + relativedelta(weeks=+d3["time"]) for in d3]
print(d3["Date1"])
d3["Date"]=d3["year"].apply(str)+"_"+d3["Date1"].apply(str)

d3['Date'] = pd.Categorical(d3['Date'],['2015_1', '2015_2', '2015_3', '2015_4', '2015_5', '2015_6', '2015_7', '2015_8', '2015_9','2015_10', '2015_11', '2015_12', '2016_1', '2016_\
2', '2016_3', '2016_4', '2016_5', '2016_6', '2016_7', '2016_8', '2016_9', '2016_10', '2016_11', '2016_12','2017_1', '2017_2', '2017_3', '2017_4', '2017_5', '2017_6', '2017_7', '2017_8', '2017_9', '2017_10', '2017_11', '2017_12','2018_1', '2018_2', '2018_3', '2018_4', '2018_5', '2018_6', '2018_7', '2018_8', '2018_9', '2018_10', '2018_11', '2018_12','2019_1', '2019_2', '2019_3', '2019_4', '2019_5', '2019_6', '2019_7', '2019_8', '2019_9', '2019_10', '2019_11', '2019_12','2020_1',  '2020_2', '2020_3', '2020_4', '2020_5', '2020_6', '2020_7', '2020_8', '2020_9', '2020_10', '2020_11', '2020_12','2021_1', '2021_2', '2021_3', '2021_4', '2021_5', '2021_6','2021_7','2021_8','2021_9'])
print(d3["Date"])

df0=d3.sort_values('Date').groupby(['Date'])["deaths"].sum().reset_index().sort_values('Date')

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
#####plt.plot(x,y,label='All deaths')
'''
plt.plot(range(0,12),y[:12],label='2015')
plt.plot(range(0,12),y[12:24],label='2016')
plt.plot(range(0,12),y[24:36],label='2017')
plt.plot(range(0,12),y[36:48],label='2018')
plt.plot(range(0,12),y[48:60],label='2019')
plt.plot(range(0,12),y[60:72],label='2020')
plt.plot(range(0,9),y[72:81],label='2021')
print(y[:12],y[72:])
2021	9.929	0.680%
2020	9.862	0.680%
2019	9.795	0.690%
2018	9.728	0.370%
2017	9.692	0.370%
2016	9.656	0.380%
2015	9.619	0.380%

'''
plt.plot(range(2015,2022),[sum(y[:12]),sum(y[12:24]),sum(y[24:36]),sum(y[36:48]),sum(y[48:60]),sum(y[60:72]),sum(y[72:81])],label='EM dataset')
plt.plot(range(2015,2022),[9.619*5531,9.656*5531,9.692*5531,9.728*5531,9.795*5531,9.862*5531,9.929*5531],label='Macrotrends dataset')
plt.title(country+" (grouped by years)")
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
print(d4)
d4['year']=[str(x) for x in pd.DatetimeIndex(d4['date']).year.to_list()]
d4['month']=[str(x) for x in pd.DatetimeIndex(d4['date']).month.to_list()]
d4["Date"]=pd.to_datetime(d4['date']).dt.strftime('%M')# - pd.to_timedelta(7, unit='d')

d4["Date"]=d4["year"]+"_"+d4["month"]

dd1=[]
ind=0
for el in d4['year'].to_list():
    dd1.append(datetime.date(int(el), 1, 1) + relativedelta(weeks=+pd.DatetimeIndex(d4['date']).month.to_list()[ind]))
    ind+=1
d4["Date1"]=[str(x) for x in pd.DatetimeIndex(dd1).month.to_list()]
d4["Date1"]=d4["Date"]
#d4['year']+"_"+d4["Date1"]
print(d4["Date1"])
d4['Date'] = pd.Categorical(d4['Date'], ['2020_1',  '2020_2', '2020_3', '2020_4', '2020_5', '2020_6', '2020_7', '2020_8', '2020_9', '2020_10', '2020_11', '2020_12','2021_1', '2021_2', '2021_3', '2021_4', '2021_5', '2021_6','2021_7','2021_8','2021_9'])

#'2020_1', '2020_2','2020_3','2020_4', '2020_5', '2020_6', '2020_7', '2020_8', '2020_9','2020_10', '2020_11', '2020_12', '2020_13', '2020_14', '2020_15', '2020_16', '2020_17', '2020_18', '2020_19', '2020_20', '2020_21', '2020_22', '2020_23', '2020_24', '2020_25', '2020_26', '2020_27', '2020_28', '2020_29','2020_30', '2020_31', '2020_32', '2020_33', '2020_34', '2020_35', '2020_36', '2020_37', '2020_38', '2020_39', '2020_40', '2020_41', '2020_42', '2020_43', '2020_44', '2020_45', '2020_46', '2020_47', '2020_48', '2020_49',  '2020_50', '2020_51', '2020_52', '2020_53', '2021_1', '2021_2','2021_3','2021_4','2021_5', '2021_6', '2021_7', '2021_8', '2021_9','2021_10', '2021_11', '2021_12', '2021_13', '2021_14', '2021_15', '2021_16', '2021_17', '2021_18', '2021_19', '2021_20','2021_21', '2021_22', '2021_23', '2021_24', '2021_25', '2021_26', '2021_27', '2021_28', '2021_29', '2021_30', '2021_31', '2021_32', '2021_33', '2021_34', '2021_35', '2021_36'])

#'2020_4', '2020_8', '2020_12', '2020_16', '2020_20', '2020_24', '2020_28', '2020_32', '2020_36','2020_40', '2020_44', '2020_48', '2021_4', '2021_8', '2021_12', '2021_16', '2021_20', '2021_24', '2021_28', '2021_32', '2021_36','2021_40'])
#print(d4["Date"])

d5=d4[["Date",country]]
print(d4)
#print(pd.DatetimeIndex(d4['date']).year.to_list())
#d4['Date'] = pd.to_datetime(d4['date']) - pd.to_timedelta(7, unit='d')
df = d5.groupby(['Date'])[country].sum().reset_index().sort_values('Date')
#print(df)
#df.drop([21])
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
#######plt.plot(x1,y1,label='Deaths from COVID-19')
#plt.title(country)
#plt.xticks(x1,y1)                                                                                                                                                                  plt.xticks(rotation=70) 
#locs, labels = plt.xticks()
'''
every_nth = 5
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)  
#plt.setp(labels, rotation=90)
'''
plt.legend()
plt.show()
