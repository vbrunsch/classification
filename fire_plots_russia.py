import pandas as pd
import json
import geopandas as gpd
import os
#https://jeetiss.github.io/covid19-russia/timeseries.json
all_data=[]
os.system("rm timeseries.json")
os.system("wget https://jeetiss.github.io/covid19-russia/timeseries.json")

with open('timeseries.json','r') as fp:
    data=json.load(fp)
    main=data['Москва']
    #date confirmed deaths recovered
    for el in list(data.keys()):
        init=[]
        #print(el,len(data[el]),len(main))
        if len(data[el])<len(main):
            ll=len(main)-len(data[el])
            #print(ll)
            for item in range(0,ll):
                init.append({"date":main[item]["date"],"confirmed":0,"deaths":0,"recovered":0,"place":el})
        #else:
        #    print("continue")
        ll1=len(data[el])
        for  item in	data[el]:
            init.append({"date":item["date"],"confirmed":item["confirmed"],"deaths":item["deaths"],"recovered":item["recovered"],"place":el})
        try:
            all_data.append(pd.DataFrame(init))
            #print(el,pd.DataFrame(init))
        except:
            print(el)
main=pd.concat(all_data)
main["date"]=pd.to_datetime(main["date"],format="%Y-%m-%d")
data=main.pivot(index='date', columns='place', values='confirmed').fillna(0)  
#print(data['Ярославская область'].to_list())    
#2020-03-22    
'''
data_=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv", index_col=0)
#print(data)
#data9=data_.T
data=data9.drop(['iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State','Country_Region', 'Lat', 'Long_', 'Combined_Key'])
print(data.index)
data0=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
data10=data0[["UID","Province_State"]].reset_index(drop=True)
data11=data0[["UID","Admin2"]].reset_index(drop=True)
ll=dict(data10.values)
ll2=dict(data11.values)
print(ll)
'''
#data["date"]=pd.to_datetime(data.index,format="%Y-%m-%d")
#data            concelho  confirmados_14
print(data)
data2=data
print(data2.columns)
for item in data2.columns:
    if item!="date":
        print(data2[item])
        data2[item]=pd.to_numeric(data2[item]).diff()
        
print(data2)
ll2=main["date"].to_list()
ll=list(data2.columns)
#data.pivot(index='data', columns='concelho', values='confirmados_14')
cols=list(data2.columns)
cols1=list([str(x).split(" ")[0] for x in data2.index])

item0=0
arrs=[]
for item in data2.fillna(0).iterrows():
    it=0
    for el in item[1].values:
        if cols[it]!="date":#,ll[cols[it]])
            print(el)
            #if el<0:
            #    el=0
            print(cols1[item0])
            print(cols[it])
            print(el)
            print(cols[it])
            arrs.append({"x":str(cols1[item0]),"y":str(cols[it]),"z":int(el),"p":'Russia'})
        it+=1
    item0+=1
print(arrs)    
print(cols)
print(cols1)

with open("fire_russia.json", "w") as fp:
    json.dump(arrs,fp)
