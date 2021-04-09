import pandas as pd
import json
import geopandas as gpd
data_=pd.read_csv("Africa_4_8_21.csv", index_col=0).sort_values(by=['Country/Region'])#.sort(['Country/Region'], ascending=[1])
#print(data)
data9=data_.T
data=data9.drop(['Province/State','Country/Region', 'Lat', 'Long'])
print(data_.index)

rr=list(data_.index)#[:len(list(data.index))-1]
data0=pd.read_csv("Africa_4_8_21.csv").sort_values(by=['Country/Region'])
data10_=pd.DataFrame()
data10_["Country/Region"]=data0["Country/Region"]
data10_["ind"]=rr
data10=data10_[["ind","Country/Region"]].reset_index(drop=True)
data11=data10_[["ind","Country/Region"]]#.reset_index(drop=True)
ll=dict(data10.values)
print(ll)
ll2=dict(data11.values)
print(ll2)

data["data"]=pd.to_datetime(data.index,format="%m/%d/%y")
#data            concelho  confirmados_14
data2=data
print(data2.columns)
for item in data2.columns:
    if item!="data":
        data2[item]=data2[item].diff()
print(data2)
#data.pivot(index='data', columns='concelho', values='confirmados_14')
cols=list(data2.columns)
cols1=list([str(x).split(" ")[0] for x in data2.index])

item0=0
arrs=[]
for item in data2.fillna(0).iterrows():
    it=0
    for el in item[1].values:
        if cols[it]!="data":#,ll[cols[it]])
            if el<0:
                el=0
            arrs.append({"x":str(cols1[item0]),"y":ll2[int(cols[it])],"z":int(el),"p":"Africa"})#,"p":ll[cols[it]]})
        it+=1
    item0+=1
print(arrs)    
#print(cols)
#print(cols1)

with open("fire_africa.json", "w") as fp:
    json.dump(arrs,fp)
