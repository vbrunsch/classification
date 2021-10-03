
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
d3["Date"]=d3["year"].apply(str)+"_"+d3["time"].apply(str)
print(len(['2015_1','2015_2','2015_3','2015_4','2015_5','2015_6','2015_7','2015_8','2015_9','2015_10', '2015_11', '2015_12', '2015_13', '2015_14', '2015_15', '2015_16', '2015_17', '2015_18', '2015_19','2015_20', '2015_21', '2015_22', '2015_23', '2015_24', '2015_25', '2015_26', '2015_27', '2015_28', '2015_29', '2015_30', '2015_31', '2015_32', '2015_33', '2015_34', '2015_35', '2015_36', '2015_37', '2015_38', '2015_39', '2015_40', '2015_41', '2015_42', '2015_43', '2015_44', '2015_45', '2015_46', '2015_47', '2015_48', '2015_49', '2015_50', '2015_51', '2015_52', '2015_53', '2016_1', '2016_2','2016_3','2016_4','2016_5','2016_6','2016_7','2016_8','2016_9','2016_10', '2016_11', '2016_12', '2016_13', '2016_14', '2016_15', '2016_16', '2016_17', '2016_18', '2016_19', '2016_20', '2016_21', '2016_22', '2016_23', '2016_24', '2016_25', '2016_26', '2016_27', '2016_28','2016_29', '2016_30', '2016_31', '2016_32', '2016_33', '2016_34', '2016_35', '2016_36', '2016_37', '2016_38', '2016_39', '2016_40', '2016_41', '2016_42', '2016_43', '2016_44', '2016_45', '2016_46', '2016_47', '2016_48', '2016_49', '2016_50', '2016_51', '2016_52',  '2017_1', '2017_2','2017_3','2017_4','2017_5','2017_6','2017_7','2017_8','2017_9','2017_10','2017_11', '2017_12', '2017_13', '2017_14', '2017_15', '2017_16', '2017_17', '2017_18', '2017_19', '2017_20', '2017_21', '2017_22', '2017_23', '2017_24', '2017_25', '2017_26', '2017_27', '2017_28', '2017_29', '2017_30', '2017_31', '2017_32', '2017_33', '2017_34', '2017_35', '2017_36', '2017_37', '2017_38', '2017_39',  '2017_40', '2017_41', '2017_42', '2017_43', '2017_44', '2017_45', '2017_46', '2017_47', '2017_48', '2017_49',  '2017_50', '2017_51', '2017_52','2018_1', '2018_2','2018_3','2018_4','2018_5','2018_6','2018_7','2018_8','2018_9','2018_10', '2018_11', '2018_12', '2018_13', '2018_14', '2018_15', '2018_16', '2018_17', '2018_18', '2018_19', '2018_20', '2018_21', '2018_22', '2018_23', '2018_24', '2018_25', '2018_26', '2018_27', '2018_28', '2018_29', '2018_30', '2018_31', '2018_32', '2018_33', '2018_34', '2018_35', '2018_36', '2018_37', '2018_38', '2018_39', '2018_40', '2018_41', '2018_42', '2018_43', '2018_44', '2018_45', '2018_46', '2018_47', '2018_48', '2018_49',  '2018_50', '2018_51', '2018_52', '2019_1', '2019_2','2019_3','2019_4','2019_5','2019_6','2019_7','2019_8','2019_9','2019_10', '2019_11', '2019_12', '2019_13', '2019_14', '2019_15', '2019_16', '2019_17', '2019_18', '2019_19', '2019_20', '2019_21', '2019_22', '2019_23', '2019_24', '2019_25', '2019_26', '2019_27', '2019_28', '2019_29','2019_30', '2019_31', '2019_32', '2019_33', '2019_34', '2019_35', '2019_36', '2019_37', '2019_38', '2019_39', '2019_40', '2019_41', '2019_42', '2019_43', '2019_44', '2019_45', '2019_46', '2019_47', '2019_48', '2019_49', '2019_50', '2019_51', '2019_52', '2020_1', '2020_2','2020_3','2020_4', '2020_5', '2020_6', '2020_7', '2020_8', '2020_9','2020_10', '2020_11', '2020_12', '2020_13', '2020_14', '2020_15', '2020_16', '2020_17', '2020_18', '2020_19', '2020_20', '2020_21', '2020_22', '2020_23', '2020_24', '2020_25', '2020_26', '2020_27', '2020_28', '2020_29','2020_30', '2020_31', '2020_32', '2020_33', '2020_34', '2020_35', '2020_36', '2020_37', '2020_38', '2020_39', '2020_40', '2020_41', '2020_42', '2020_43', '2020_44', '2020_45', '2020_46', '2020_47', '2020_48', '2020_49',  '2020_50', '2020_51', '2020_52', '2020_53', '2021_1', '2021_2','2021_3','2021_4','2021_5', '2021_6', '2021_7', '2021_8', '2021_9','2021_10', '2021_11', '2021_12', '2021_13', '2021_14', '2021_15', '2021_16', '2021_17', '2021_18', '2021_19', '2021_20','2021_21', '2021_22', '2021_23', '2021_24', '2021_25', '2021_26', '2021_27', '2021_28', '2021_29', '2021_30', '2021_31', '2021_32', '2021_33', '2021_34', '2021_35', '2021_36']))
d3['Date'] = pd.Categorical(d3['Date'],['2015_1', '2015_2','2015_3','2015_4','2015_5','2015_6','2015_7','2015_8','2015_9','2015_10', '2015_11', '2015_12', '2015_13', '2015_14', '2015_15', '2015_16', '2015_17', '2015_18', '2015_19','2015_20', '2015_21', '2015_22', '2015_23', '2015_24', '2015_25', '2015_26', '2015_27', '2015_28', '2015_29', '2015_30', '2015_31', '2015_32', '2015_33', '2015_34', '2015_35', '2015_36', '2015_37', '2015_38', '2015_39', '2015_40', '2015_41', '2015_42', '2015_43', '2015_44', '2015_45', '2015_46', '2015_47', '2015_48', '2015_49', '2015_50', '2015_51', '2015_52', '2015_53', '2016_1', '2016_2','2016_3','2016_4','2016_5','2016_6','2016_7','2016_8','2016_9','2016_10', '2016_11', '2016_12', '2016_13', '2016_14', '2016_15', '2016_16', '2016_17', '2016_18', '2016_19', '2016_20', '2016_21', '2016_22', '2016_23', '2016_24', '2016_25', '2016_26', '2016_27', '2016_28', '2016_29', '2016_30', '2016_31', '2016_32', '2016_33', '2016_34', '2016_35', '2016_36', '2016_37', '2016_38', '2016_39', '2016_40', '2016_41', '2016_42', '2016_43', '2016_44', '2016_45', '2016_46', '2016_47', '2016_48', '2016_49', '2016_50', '2016_51', '2016_52',  '2017_1', '2017_2','2017_3','2017_4','2017_5','2017_6','2017_7','2017_8','2017_9','2017_10', '2017_11', '2017_12', '2017_13', '2017_14', '2017_15', '2017_16', '2017_17', '2017_18', '2017_19', '2017_20', '2017_21', '2017_22', '2017_23', '2017_24', '2017_25', '2017_26', '2017_27', '2017_28', '2017_29', '2017_30', '2017_31', '2017_32', '2017_33', '2017_34', '2017_35', '2017_36', '2017_37', '2017_38', '2017_39',  '2017_40', '2017_41', '2017_42', '2017_43', '2017_44', '2017_45', '2017_46', '2017_47', '2017_48', '2017_49',  '2017_50', '2017_51', '2017_52','2018_1', '2018_2','2018_3','2018_4','2018_5','2018_6','2018_7','2018_8','2018_9','2018_10', '2018_11', '2018_12', '2018_13', '2018_14', '2018_15', '2018_16', '2018_17', '2018_18', '2018_19', '2018_20', '2018_21', '2018_22', '2018_23', '2018_24', '2018_25', '2018_26', '2018_27', '2018_28', '2018_29', '2018_30', '2018_31', '2018_32', '2018_33', '2018_34', '2018_35', '2018_36', '2018_37', '2018_38', '2018_39', '2018_40', '2018_41', '2018_42', '2018_43', '2018_44', '2018_45', '2018_46', '2018_47', '2018_48', '2018_49',  '2018_50', '2018_51', '2018_52', '2019_1', '2019_2','2019_3','2019_4','2019_5','2019_6','2019_7','2019_8','2019_9','2019_10', '2019_11', '2019_12', '2019_13', '2019_14', '2019_15', '2019_16', '2019_17', '2019_18', '2019_19', '2019_20', '2019_21', '2019_22', '2019_23', '2019_24', '2019_25', '2019_26', '2019_27', '2019_28', '2019_29','2019_30', '2019_31', '2019_32', '2019_33', '2019_34', '2019_35', '2019_36', '2019_37', '2019_38', '2019_39', '2019_40', '2019_41', '2019_42', '2019_43', '2019_44', '2019_45', '2019_46', '2019_47', '2019_48', '2019_49', '2019_50', '2019_51', '2019_52', '2020_1', '2020_2','2020_3','2020_4', '2020_5', '2020_6', '2020_7', '2020_8', '2020_9','2020_10', '2020_11', '2020_12', '2020_13', '2020_14', '2020_15', '2020_16', '2020_17', '2020_18', '2020_19', '2020_20', '2020_21', '2020_22', '2020_23', '2020_24', '2020_25', '2020_26', '2020_27', '2020_28', '2020_29','2020_30', '2020_31', '2020_32', '2020_33', '2020_34', '2020_35', '2020_36', '2020_37', '2020_38', '2020_39', '2020_40', '2020_41', '2020_42', '2020_43', '2020_44', '2020_45', '2020_46', '2020_47', '2020_48', '2020_49',  '2020_50', '2020_51', '2020_52', '2020_53', '2021_1', '2021_2','2021_3','2021_4','2021_5', '2021_6', '2021_7', '2021_8', '2021_9','2021_10', '2021_11', '2021_12', '2021_13', '2021_14', '2021_15', '2021_16', '2021_17', '2021_18', '2021_19', '2021_20','2021_21', '2021_22', '2021_23', '2021_24', '2021_25', '2021_26', '2021_27', '2021_28', '2021_29', '2021_30', '2021_31', '2021_32', '2021_33', '2021_34', '2021_35', '2021_36'])
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
plt.plot(x,y,label='All deaths')
plt.title(country+" (grouped by weeks)")
#plt.locator_params(axis='x', nbins=20)
#fig, ax = plt.subplots()
#print(x)
#plt.plot(...)
#print(ax.xaxis.get_ticklabels())
every_nth = 10
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
#plt.show()



data2=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_deaths.csv").fillna(0)
#x1=range(0,len(data2["date"]))
#y1=data2["Ireland"].to_list()

d4=data2[["date",country]]
d4['year']=[str(x) for x in pd.DatetimeIndex(d4['date']).year.to_list()]
d4['month']=[str(x*4) for x in pd.DatetimeIndex(d4['date']).month.to_list()]
d4["Date"]=pd.to_datetime(d4['date']).dt.strftime('%W')# - pd.to_timedelta(7, unit='d')
d4["Date"]=d4["year"]+"_"+d4["Date"]
d4['Date'] = pd.Categorical(d4['Date'], ['2020_1', '2020_2','2020_3','2020_4', '2020_5', '2020_6', '2020_7', '2020_8', '2020_9','2020_10', '2020_11', '2020_12', '2020_13', '2020_14', '2020_15', '2020_16', '2020_17', '2020_18', '2020_19', '2020_20', '2020_21', '2020_22', '2020_23', '2020_24', '2020_25', '2020_26', '2020_27', '2020_28', '2020_29','2020_30', '2020_31', '2020_32', '2020_33', '2020_34', '2020_35', '2020_36', '2020_37', '2020_38', '2020_39', '2020_40', '2020_41', '2020_42', '2020_43', '2020_44', '2020_45', '2020_46', '2020_47', '2020_48', '2020_49',  '2020_50', '2020_51', '2020_52', '2020_53', '2021_1', '2021_2','2021_3','2021_4','2021_5', '2021_6', '2021_7', '2021_8', '2021_9','2021_10', '2021_11', '2021_12', '2021_13', '2021_14', '2021_15', '2021_16', '2021_17', '2021_18', '2021_19', '2021_20','2021_21', '2021_22', '2021_23', '2021_24', '2021_25', '2021_26', '2021_27', '2021_28', '2021_29', '2021_30', '2021_31', '2021_32', '2021_33', '2021_34', '2021_35', '2021_36'])

#'2020_4', '2020_8', '2020_12', '2020_16', '2020_20', '2020_24', '2020_28', '2020_32', '2020_36','2020_40', '2020_44', '2020_48', '2021_4', '2021_8', '2021_12', '2021_16', '2021_20', '2021_24', '2021_28', '2021_32', '2021_36','2021_40'])
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
plt.plot(x1,y1,label='Deaths from COVID-19')
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
