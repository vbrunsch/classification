
1;95;0c
#/Users/olgabuchel/Downloads/28_day.csv - last 28 days
#OBJECTID	Place	תאריך	שעות שהייה	x	y
#1276117	פינסקר - מרכז מקצועי - שירותי בריאות כללית - ראשון לציון	28/6/2020	08:00 - 10:30	34.80713460000000	31.968514200000100
#/Users/olgabuchel/Downloads/IRSL.csv - historical dates grouped
#	City	Population as of 2018	Number of tests so far	Verified patients discovered so far	Number of recoverers	The growth rate of verified patients in the last 3 days	The number of verified patients added in the last 3 days	Actual morbidity rate ** per 100,000	dates
#https://imoh.maps.arcgis.com/apps/webappviewer/index.html?id=20ded58639ff4d47a2e2e36af464c36e&locale=he&/
#/Users/olgabuchel/Downloads/coordinates.csv 
#prepare_classification_counties_israel2.py
#'IL': ('Israel', (34.2654333839, 29.5013261988, 35.8363969256, 33.2774264593)),

import csv
import json
#/Users/olgabuchel/Downloads/gridtest (1).json 
#create a dictionary of names and coordinates. Coords are in 28 days
#add coordinates to the historical data
#{'type': 'GeometryCollection', 'geometries': [{'type': 'MultiLineString', 'coordinates':
ffs={}
ffs["type"]="FeatureCollection"
ffs["features"]=[]
with open('/Users/olgabuchel/Downloads/gridtest (1).json', 'r') as jsonfile:
    data=json.load(jsonfile)
    ind=0
    for item in data["geometries"][0]["coordinates"]:
        feature={}
        feature["type"]="Feature"
        feature["geometry"]={"type":"Polygon","coordinates":[item]}
        feature["properties"]={"name":"feature_"+str(ind)}
        #print(feature)
        ffs["features"].append(feature)
        ind+=1
print(ffs)
with open('grid_israel.json', 'w') as jsonfile:
    json.dump(ffs,jsonfile)
coords={}
with open('/Users/olgabuchel/Downloads/28_day.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if row[1] not in list(coords.keys()):
            coords[row[1]]=[row[4],row[5]]
#print(coords)
        

''''
import json

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
#from prep_canada_data import stage_latest
date_of_analysis='7/11/20'
df = pd.read_csv('/Users/olgabuchel/Downloads/14_day.csv')
print(list(df.columns))
print(df[list(df.columns)[1]])
print(df[list(df.columns)[2]])
print(df[list(df.columns)[4]])
print(df[list(df.columns)[5]])
df2=df.groupby([list(df.columns)[1],list(df.columns)[2],list(df.columns)[4],list(df.columns)[5]]).count().reset_index()
#print(df2)
df4=pd.pivot_table(df2,index=[list(df.columns)[2]],columns=list(df.columns)[1],values=["OBJECTID"],aggfunc=np.sum)


output_directory = 'output_israel'
os.makedirs(output_directory + '/classification', exist_ok=True)


e_dataframe0=df2

ids = list(df4.columns)[3:]
#list(df2.Place.unique())  
recs = list(df4.columns)[3:]
#list(df2.Place.unique())

#print(df2.index)


# stage latest Canada HR-level data for later processing
#latest_ca_df = stage_latest()
#print(latest_ca_df)
#assert latest_ca_df.index.names == ['Combined_Key']
#print(latest_ca_df)

#e_dataframe0 = e_dataframe.drop(columns=['UID','iso2','iso3','code3','FIPS','Admin2','Province_State','Country_Region','Lat','Long_'])
e_dataframe1 = df4
#pd.pivot_table(df4,index=["dates"],columns='Combined_Key',values=["Confirmed Cases Count"],aggfunc=np.sum).fillna(0)
#print(e_dataframe1)
#print(ids)
#print(recs)


def add_day_columns(df):
    """Add columns Elapsed_days, Decimals, Day_Year to df."""
    dats = list(df.index)
    #print(dats)
    dats2 = []
    decimals = []
    elapsed_days = []
    ind = 35
    for el in dats:
        dats2.append(ind)
        dec = 2020 + (ind / 366)
        elapsed_days.append(ind - 20)
        decimals.append(dec)
        ind += 1
    df.insert(0, "Day_Year", dats2, True)
    df.insert(0, "Decimals", decimals, True)
    df.insert(0, "Elapsed_days", elapsed_days, True)


add_day_columns(e_dataframe1)
#print(e_dataframe1)


if False:
    # show intermediate result and abortthe script right here
    print(e_dataframe1.iloc[10:, :5])
    import sys
    sys.exit(0)

tim = list(df[list(df.columns)[2]].unique())
print(tim)
tim.pop(0)

ind4 = 0
aar = []
aar1 = []
counties = list(df4.columns)[3:]
print(counties)
#e_dataframe1.columns[3:]


def compute_original_values(values):
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
        if recent_mean >= threshold:
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

print(df4.columns)
for name in counties:
    name0=name[1]
    #print(name)
    values = e_dataframe1[name].fillna(0).cumsum()
    #print(values)        
    
    num_rows = len(values)
    y50 = values[-12:]
    #print(y50)
    y5 = [y - values[len(values)-12] for y in y50]
    y = values
    original_values = compute_original_values(values)
    #print(original_values)
    
    x = e_dataframe1[e_dataframe1.columns[0]]
    y1 = interpolate(y)
    print(x,y1)
    
    x2 = x[6:]
    tim2 = tim[3 : -4]
    #print(tim2)
    y3 = pd.DataFrame(y1, columns=["a"]).rolling(window=7).mean()['a'].to_list()[6:]
    ys = y3[-12:]
    xs = x[-9:-4]  # last 24 days
    ind2 = 0
    start = []
    start2 = []
    if int(np.max(y)) > 0:
        vv = [int(x) for x in y.to_list() if x != min(y3)]
        start.append(y.to_list().index(vv[0]))
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
            color="darkseagreen"

        print(name[1],color,ratio,recent_mean0,int(max(y5)))#,str(ids[recs.index(name)]["Combined_Key"]))
        print(y5)
        print(y3)
        print(y)
        
        plt.title(name[1])                                                                                                                                           
        plt.plot(x2,y3,color=color)                                                                                                                                      
        plt.savefig(name[1]+".png")                                                                                                                                         
        plt.show()          
        
        try:        
            with open(output_directory + '/classification/data_counties_'+str(ids[recs.index(name)])+'.json', 'w') as outfile:
                json.dump({"dates":tim2,"max_14": int(max(y5)-min(y5)),"max":int(max(y)),"value":y3,"time":tim,"original_values":original_values},outfile)
                #aar.append({"color":color,"province":name.split(",")[0],"country":name.split(",")[1],"id":"new_id_"+str(ind4),"value1":ratio, "dates":tim2,"value":y3})
            aar1.append({"n":name,"id":ids[recs.index(name)],"v":ratio,"c":color,"max":int(max(y5)-min(y5)),"t":int(max(y))})
        except:
            continue
        ind4+=1


# with open('classification/data_counties.json', 'w') as outfile:
#    json.dump(aar,outfile)
print(aar1)
aar1[0]["date"]=date_of_analysis
# this file is used by the map
with open(output_directory + '/classification/classification_ids_counties2.json', 'w') as outfile:
    json.dump(aar1, outfile)


'''
