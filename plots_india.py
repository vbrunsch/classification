import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
import urllib.request, json
import seaborn as sns
from scipy import stats as sps
import matplotlib.colors as mcolors

#from src.data_collection import *
#from src.constants import *

import pandas as pd
import json
import geopandas as gpd
#data_1=pd.read_csv("../Covid19Casos.csv", index_col=0)
#print(data_1.columns)
#print(data_['clasificacion_resumen'].unique())#'clasificacion', 'clasificacion_resumen'
#data_=data_1[data_1['clasificacion_resumen']=="Confirmado"]
#data=data_.groupby(['fecha_diagnostico','residencia_provincia_nombre']).count().reset_index()
#print(data)
#data2=pd.pivot_table(data=data,index="fecha_diagnostico",columns='residencia_provincia_nombre', values='sexo').fillna(0)
#print(data2)


df = pd.read_csv('https://raw.githubusercontent.com/coder-amey/COVID-19-India_Data/master/time-series/India_aggregated.csv')
df = df.pivot(index='Date', columns='Region', values='Confirmed')#Confirmed')
df.index = pd.to_datetime(df.index, dayfirst=True, format='%d-%m-%Y')
df.sort_index(inplace=True)
df.drop('National Total', inplace=True, axis=1)
data2 = df[df.sum().sort_values(ascending=False).index].diff().fillna(0).astype(int)
print(data2)
cols=list(data2.columns)
cols1=list([str(x).split(" ")[0] for x in data2.index])
kkd0=data2.sum(axis = 0, skipna = True).to_dict()
'''
data13=pd.read_csv("argentina_population.csv")
data13["Population (2013)1"]=[int(str(x).replace(",","")) for x in data13["Population (2013)"].to_list()]
kkd=data13[["Province/District","Population (2013)1"]].set_index("Province/District").to_dict()["Population (2013)1"]
'''
all=[]
for item in list(kkd0.keys()):
    try:
        all.append([item,kkd0[item],kkd[item],kkd0[item]/kkd[item]])
    except:
        all.append([item,kkd0[item],0,kkd0[item]])

dd=pd.DataFrame(all,columns=["Province","Cases","Population","Ratio"])
dd0=dd.sort_values(by=['Ratio'], ascending=False)
print(dd0)
print(dd0["Province"].to_list())
item0=0
arrs=[]
for item in data2.iterrows():
    it=0
    for el in item[1].values:
        if cols[it]!="data":#,ll[cols[it]])
            if el<0:
                el=0
            arrs.append({"x":cols1[item0],"y":str(cols[it]),"z":int(el),"p":"India"})
        it+=1
    item0+=1

for item in dd0["Province"].to_list():
    print(item,data2[item])
#print(arrs)    
#print(cols)
#print(cols1)
#print(kkd)
#print(kkd0)
#with open("fire_india.json", "w") as fp:
#    json.dump(arrs,fp)
colors=mcolors.CSS4_COLORS
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))),name) for name, color in colors.items())
names = [name for hsv, name in by_hsv]
print(names)
fig, ax=plt.subplots(nrows=1, ncols=1, figsize=(8,7))
ind=0
for item in dd0["Province"].to_list():
    t1 = data2[item]
    print(t1)
    ax.plot(t1.rolling(window=7, min_periods=1, center=True).mean(std=2),names[ind], label='%s 7-day average'%item)
    #ax.plot(t1.diff(),'o', c='C'+str(ind), alpha=0.5)                                                                                                                               
    ind+=1


#ax.legend(fontsize=10)
ax.tick_params(labelsize=10)
ax.legend(loc=0, fontsize=6)
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.tight_layout()
ax.grid(alpha=0.6)
plt.show()
#plt.savefig(r'figures/Prov_vs_prov2_comparison_%s.png'% (state + state2 + state3 + date), dpi=50)
