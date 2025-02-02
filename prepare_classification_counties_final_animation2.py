

import json
import numpy as np
import pandas as pd
import os
from datetime import date
date_of_analysis=date.today().strftime("%m/%d/%y")
print(date_of_analysis)

output_directory = 'output'
os.makedirs(output_directory + '/classification', exist_ok=True)
# Use canned CSV file, so we can compare results to earlier runs of the script.
use_canned_file = False

if use_canned_file:
    data = pd.read_csv('data/time_series/time_series_covid19_confirmed_US.csv')
    assert data.columns[-1] == date_of_analysis
else:
    # Original:
    #data = pd.read_csv('data/time_series/time_series_covid19_confirmed_US.csv')
    data0 = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
#date          state  fips   cases  deaths 2020-01-21
#data0["date"]=pd.to_datetime(data0["date"],format="%Y-%m-%d")
data=pd.pivot_table(data0, values='cases', index=["date"],columns=['state'], aggfunc=np.sum).fillna(0)
print(data.index)
#tim=list(data.columns)

e_dataframe = pd.pivot_table(data0, values='cases', index=["state"],columns=['date'], aggfunc=np.sum).fillna(0)
#data_.reset_index()
ids = list(data.columns)
#[["Province_State"]].to_dict('records')
recs = ids
#data["Province_State"].to_list()



e_dataframe0 = e_dataframe#.drop(columns=['UID','iso2','iso3','code3','FIPS','Admin2','Combined_Key','Country_Region','Lat','Long_'])
e_dataframe1=e_dataframe0.transpose()


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


add_day_columns(e_dataframe1)
#print(e_dataframe1)


if False:
    # show intermediate result and abortthe script right here
    print(e_dataframe1.iloc[10:, :5])
    import sys
    sys.exit(0)

#tim = list(e_dataframe0.columns)
#tim.pop(0)

ind4 = 0
aar = []
aar1 = []
counties = recs
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
all_states={}
all_dates=list(e_dataframe.columns)[30:50]
for item in all_dates:
    rm=all_dates[all_dates.index(item):]
    #print(e_dataframe0.drop(columns=rm))                                                                                                                                            
    e_dataframe1 = e_dataframe0.drop(columns=rm).transpose()
    #print(e_dataframe1)
    tim=list(e_dataframe1.columns)
    for name in counties:
        values = e_dataframe1[name]
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
                color="darkgreen"
            if name not in list(all_states.keys()):    
                all_states[name]={}
                all_states[name][item]=color
            else:
                all_states[name][item]=color                
                #print(item,name,color,ratio,recent_mean0,int(max(y5)))
            '''
            with open(output_directory + '/classification/data_counties_'+str(ids[recs.index(name)]["UID"])+'.json', 'w') as outfile:
                json.dump({"dates":tim2,"max_14": int(max(y5)-min(y5)),"max":int(max(y)),"value":y3,"time":tim,"original_values":original_values},outfile)
            #aar.append({"color":color,"province":name.split(",")[0],"country":name.split(",")[1],"id":"new_id_"+str(ind4),"value1":ratio, "dates":tim2,"value":y3})
            aar1.append({"n":name,"id":ids[recs.index(name)]["UID"],"v":ratio,"c":color,"max":int(max(y5)-min(y5))})
            '''
            ind4+=1
print(all_states)    
'''
# with open('classification/data_counties.json', 'w') as outfile:
#    json.dump(aar,outfile)
aar1[0]["date"]=date_of_analysis
# this file is used by the map
with open(output_directory + '/classification/classification_ids_counties2.json', 'w') as outfile:
    json.dump(aar1, outfile)
'''
