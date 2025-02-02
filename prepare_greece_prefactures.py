#https://raw.githubusercontent.com/Sandbird/covid19-Greece/master/prefectures.csv
import json
import pandas as pd
import geopandas as gpd
import numpy as np
import os
from datetime import date

date_of_analysis=date.today().strftime("%m/%d/%y")
print(date_of_analysis)
os.system("rm prefectures.csv")
os.system("wget https://raw.githubusercontent.com/Sandbird/covid19-Greece/master/prefectures.csv")
output_directory = 'output_greece'
os.makedirs(output_directory + '/classification', exist_ok=True)

'''
with open("greece-prefectures.geojson","r") as fp:
    data=json.load(fp)
    print(data)
'''
data00=gpd.read_file("greek_prefs.json")
data0=gpd.read_file("greece-prefectures.geojson")
data=gpd.read_file("greek-features.json")
data2=pd.read_csv("prefectures.csv")
#print(data["cartodb_id"].unique())
#'NAME_GR', 'NAME_ENG'
print(data[data["NAME_GR"]=='Ν. ΑΝΑΤΟΛΙΚΗΣ ΑΤΤΙΚΗΣ'].values)
#print(data["id"].unique())
'''
print(list(data["name"].unique()))
print(list(data["cartodb_id"].unique()))
#print(data2["region_id"].unique())
print(list(data2["region_id"].unique()))
print(list(data2["region_en"].unique()))
print(data2[data2["region_id"]==13]['region_en'].unique())
print(data[data["cartodb_id"]==13]['name'].unique())
'''
#print(list(data2["region_id"].unique()))   
print(data2[data2["region_gr"]=="Άνδρου"])  
print(data0['name_greek'].unique())
print(data00.columns)

with open("greece_codes.json","r") as fp:
    kkeys=json.load(fp)#.decode("latin-1").encode("utf-8")
    #kk=json.JSONDecoder().decode(kkeys)
kkeys2={}
for item in list(kkeys.keys()):
    if type(kkeys[item])==str:
        kkeys2[kkeys[item]]=item
    else:
        for it in kkeys[item]:
            kkeys2[it]=item
print(kkeys2)
data2['region_gr1']=data2['region_gr'].map(kkeys2)
#print(data2.columns)
data3=data2.groupby(['date','region_gr1'])['cases'].sum().reset_index()
data4=data3.pivot(index='date', columns='region_gr1', values='cases')
print(list(np.array(data4['Ν. ΑΘΗΝΩΝ'].to_list()).cumsum()))

e_dataframe1=data4

def add_day_columns(df):
    """Add columns Elapsed_days, Decimals, Day_Year to df."""
    dats = list(df.index)
    # print(dats)                                                                                                                                                                   
    dats2 = []
    decimals = []
    elapsed_days = []
    ind = 22
    for el in dats:
        dats2.append(ind)
        dec = 2020 + (ind / 366)
        elapsed_days.append(ind - 20)
        decimals.append(dec)
        ind += 1
    df.insert(0, "Day_Year", dats2, True)
    df.insert(0, "Decimals", decimals, True)
    df.insert(0, "Elapsed_days", elapsed_days, True)


#add_day_columns(e_dataframe1)
#print(e_dataframe1)                                                                                                                                                                


if False:
    # show intermediate result and abortthe script right here                                                                                                                       
    print(e_dataframe1.iloc[10:, :5])
    import sys
    sys.exit(0)

tim = list(e_dataframe1.index)
#tim.pop(0)
print(tim)
ind4 = 0
aar = []
aar1 = []
counties = e_dataframe1.columns#[3:]
print(counties)

ids=counties
recs=counties
def compute_original_values(values):
    print(values)
    result = []
    ind3 = 0
    for e in values:
        if ind3 < num_rows - 1:
            result.append(int(values[ind3 + 1]) - int(e))
        else:
            print("")
            #result.append(result[-1])                                                                                                                                             
        ind3 += 1
    return result


def interpolate(y):
    ind = 0
    y1 = []
    for el in y:
        if ind >= 1 and ind <= len(y) - 2:
            y0 = (int(y[ind + 1]) - int(y[ind - 1])) / 2
            y1.append(y0)
        elif ind == 0:
            y0 = (int(y[ind + 1]) - int(el)) / 2
            y1.append(y0)
        else:
            y0 = (int(el) - int(y[ind - 1])) / 2
            y1.append(y0)
        ind += 1
    return y1


def classify(ratio, recent_mean, threshold):
    color = None
    if ratio >= 0.79:
        if recent_mean >= threshold:
            color = "red"
        else:
            color = "green"
    elif ratio <= 0.1:
        if recent_mean > threshold:
            color = "yellow"
        else:
            color = "green"
    elif ratio >= 0.4 and ratio < 0.79:
        if recent_mean >= threshold:
            color = "orange"
        else:
            color = "green"
    elif ratio > 0.1 and ratio < 0.4:
        if recent_mean >= threshold:
            color = "yellow"
        else:
            color = "green"
    assert color is not None
    return color

for name in counties:
    values = list(np.array(e_dataframe1[name].fillna(0).to_list()).cumsum())
    num_rows = len(values)
    y50 = values[-15:]
    y5 = [y - values[-15] for y in y50]
    y = values
    original_values = compute_original_values(values)
    x = e_dataframe1[e_dataframe1.columns[0]]
    y1 = interpolate(y)
    x2 = x[9:]
    tim2 = tim[3 : -4]
    y3 = pd.DataFrame(y1, columns=["a"]).rolling(window=7).mean()['a'].to_list()[6:]
    ys = y3[-24:]
    xs = x[-29:-5]  # last 24 days                                                                                                                                                  
    ind2 = 0
    start = []
    start2 = []
    if int(np.max(y)) > 0:
        vv = [int(x) for x in y if x != min(y3)]
        start.append(y.index(vv[0]))
    else:
        start.append(0)
    threshold = 1
    if len(start) > 0:
        max0 = np.max(y3)
        min0 = np.min(ys)
        recent_mean0=0
        if max0 > 0:
            ratio = y3[-1] / max0
            recent_mean = int(np.mean(original_values[-11:]))
            recent_mean0 += recent_mean
            #if recent_mean > threshold:                                                                                                                                            
            color = classify(ratio, recent_mean, threshold)
            #else:                                                                                                                                                                  
            #    color = "green"                                                                                                                                                    
        else:
            #print(name,y3)                                                                                                                                                         
            ratio=0

            color="darkgreen"

        print(name,color,ratio,recent_mean0,int(max(y5)))
        with open(output_directory + '/classification/data_counties_'+str(name)+'.json', 'w') as outfile:
            json.dump({"dates":tim2,"max_14": int(max(y5)-min(y5)),"max":int(max(y)),"value":y3,"time":tim,"original_values":original_values},outfile)
        #aar.append({"color":color,"province":name.split(",")[0],"country":name.split(",")[1],"id":"new_id_"+str(ind4),"value1":ratio, "dates":tim2,"value":y3})                   
        aar1.append({"n":name,"id":name,"v":ratio,"c":color,"max":int(max(y5)-min(y5))})
        ind4+=1

aar1[0]["date"]=date_of_analysis
# this file is used by the map

 
with open(output_directory + '/classification/classification_ids_counties2.json', 'w') as outfile:
    json.dump(aar1, outfile)

