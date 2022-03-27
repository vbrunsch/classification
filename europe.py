
from scipy import optimize
import datetime
#https://static.data.gouv.fr/resources/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19/20200829-191505/sp-pos-quot-dep-2020-08-29-19h15.csv
#https://www.data.gouv.fr/fr/datasets/r/406c6a23-e283-4300-9484-54e78c8ae675
#https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-avec-outre-mer.geojson
#https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19-france/#_
#https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19/#_
#https://epistat.wiv-isp.be/covid/COVID19BE.xslx
#https://epistat.sciensano.be/Data/COVID19BE.xlsx
#1) group by
#pivot
#https://raw.githubusercontent.com/ec-jrc/COVID-19/master/data-by-region/jrc-covid-19-all-days-by-regions.csv
#https://webcritech.jrc.ec.europa.eu/modellingoutput/cv/eu_cv_region/eu_cv_region_inf.htm
#DATE PROVINCE REGION AGEGROUP SEX  CASES

import matplotlib.pyplot as plt
import json

import numpy as np
import pandas as pd
import os
#from prep_canada_data import stage_latest
#https://cdn.mbta.com/archive/archived_feeds.txt
from datetime import date
date_of_analysis=date.today().strftime("%m/%d/%y")
print(date_of_analysis)

df = pd.read_csv('https://raw.githubusercontent.com/ec-jrc/COVID-19/master/data-by-region/jrc-covid-19-all-days-by-regions.csv')

switzerland=df[df["CountryName"]=="Switzerland"]
#print(switzerland)
portugal=df[df["CountryName"]=="Portugal"]
print(portugal)
luxembourg=df[df["CountryName"]=="Luxembourg"]
#print(luxembourg)
austria=df[df["CountryName"]=="Austria"]
#print(austria)
bulgaria=df[df["CountryName"]=="Bulgaria"]
#print(bulgaria)
italy=df[df["CountryName"]=="Italy"]
#print(italy)
poland=df[df["CountryName"]=="Poland"]
#print(poland)
czech=df[df["CountryName"]=="Czech Republic"]
#print(czech)
slovakia=df[df["CountryName"]=="Slovakia"]
#print(slovakia)
hungary=df[df["CountryName"]=="Hungary"]
#print(hungary)
norway=df[df["CountryName"]=="Norway"]
#print(norway)
finland=df[df["CountryName"]=="Finland"]
#print(finland)
romania=df[df["CountryName"]=="Romania"]
#print(romania)
croatia=df[df["CountryName"]=="Croatia"]
#print(croatia)
albania=df[df["CountryName"]=="Albania"]
#print(albania)
nmacedonia=df[df["CountryName"]=="North Macedonia"]
#print(nmacedonia)
kosovo=df[df["CountryName"]=="Kosovo"]
#print(kosovo)
serbia=df[df["CountryName"]=="Serbia"]
#print(serbia)

uk=df[df["CountryName"]=="United Kingdom"]
#print(uk)
lch=df[df["CountryName"]=="Liechtenstein"]
#print(lch)
bh=df[df["CountryName"]=="Bosnia and Herzegovina"]
#print(bh)
malta=df[df["CountryName"]=="Malta"]
#print(malta)
andorra=df[df["CountryName"]=="Andorra"]
#print(andorra)
cyprus=df[df["CountryName"]=="Cyprus"]
#print(cyprus)
#denmark=df[df["CountryName"]=="Denmark"]
#print(denmark)
denmark=df[df["CountryName"]=="Denmark"]
#print(denmark)
san_marino=df[df["CountryName"]=="San Marino"]
#print(san_marino)
montenegro=df[df["CountryName"]=="Montenegro"]
#print(montenegro)
slovenia=df[df["CountryName"]=="Slovenia"]
#print(slovenia)
print(df["CountryName"].unique())

all_countries={'Norway':norway,'Finland':finland,'Romania':romania, 'Czech Republic':czech,'Montenegro':montenegro}#{'Austria':austria,'Luxembourg':luxembourg, 'Switzerland':switzerland, 'United Kingdom':uk, 'Italy':italy}#,'Luxembourg':luxembourg,'Hungary':hungary, 'Austria':austria,'Bosnia and Herzegovina':bh,'Slovakia':slovakia, 'Malta':malta,'Norway':norway, 'Andorra':andorra,'Cyprus':cyprus, 'Denmark':denmark,'Slovenia':slovenia, 'Albania':albania, 'Finland':finland, 'Romania':romania, 'Czech Republic':czech,'Montenegro':montenegro, 'Poland':poland}#'Liechtenstein':lch,'Portugal':portugal,'Croatia':croatia,'San Marino':san_marino,'Serbia':serbia,'Bulgaria':bulgaria,'North Macedonia':nmacedonia}
print(all_countries)



'''

['France' 'Switzerland' 'United Kingdom' 'Italy' 'Latvia' 'Netherlands'
 'Germany' 'Spain' 'Belgium' 'Estonia' 'Greece' 'Luxembourg' 'Portugal'
 'Hungary' 'Ukraine' 'Austria' 'Liechtenstein' 'Bosnia and Herzegovina'
 'Slovakia' 'Malta' 'Ireland' 'Norway' 'Andorra' 'Belarus' 'Croatia'
 'Cyprus' 'Denmark' 'Lithuania' 'Moldova' 'San Marino' 'Serbia' 'Sweden'
 'Slovenia' 'Turkey' 'Albania' 'Finland' 'Romania' 'Czech Republic'
 'Iceland' 'Monaco' 'Montenegro' 'Russian Fed.' 'Bulgaria' 'Poland'
 'North Macedonia' 'Armenia']



for kkey in list(all_countries.keys()):
    df3=all_countries[kkey]
    #.dropna().groupby(["DATE","PROVINCE","REGION"])["CASES"].sum().reset_index()
    df3["Combined_Key"]=df3["Region"]+", "+df3["CountryName"]
    df4=pd.pivot_table(df3, values='CumulativePositive', index=['Combined_Key'],columns=['Date'],aggfunc=np.sum)
    print(df4)
    output_directory = 'output_'+kkey
    os.makedirs(output_directory + '/classification', exist_ok=True)
    print(output_directory)
    e_dataframe = df3.set_index("iso3")
    ids = df3[["Combined_Key"]].to_dict('records')
    recs = df3["Combined_Key"].to_list()
    e_dataframe1 = df4
    e_dataframe0=e_dataframe1.transpose()
    print(e_dataframe0)
    
'''

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

'''
if False:
    # show intermediate result and abortthe script right here
    print(e_dataframe1.iloc[10:, :5])
    import sys
    sys.exit(0)
'''


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


pop={"Aargau, Switzerland":678207, "Zug, Switzerland":29804, "Uri, Switzerland":36433,"Jura, Switzerland":73419, "Graubünden, Switzerland":198379, "Vaud, Switzerland":799145, "Thurgau, Switzerland":282909, "Ticino, Switzerland":350986, "St. Gallen, Switzerland": 75481, "Uri, Switzerland":60439692,'Solothurn, Switzerland': 16163,'Basel City, Switzerland': 194766, 'Appenzell Ausserrhoden, Switzerland': 55234 , 'Basel Country, Switzerland': 171017, 'Bern, Switzerland':  133115, 'Fribourg, Switzerland': 38829, 'Geneva, Switzerland': 198979,'Glarus, Switzerland': 12425, 'Liechtenstein, Switzerland': 38896,'Lucerne, Switzerland': 	81691, 'Neuchâtel, Switzerland': 32819,'Nidwalden, Switzerland': 43223, 'Obwalden, Switzerland': 37841,'Schaffhausen, Switzerland': 36587, 'Schwyz, Switzerland': 14183,
"Ayrshire and Arran, United Kingdom": 366800,
"Borders, United Kingdom": 115270,
"Dumfries and Galloway, United Kingdom": 148790,
"East of England, United Kingdom": 6235000,
"Eileanan Siar (Western Isles), United Kingdom": 470990,
"England, United Kingdom": 55980000,
"Fife, United Kingdom": 371910,
"Forth Valley, United Kingdom": 300000,
"Grampian, United Kingdom": 584550,
"Greater Glasgow and Clyde, United Kingdom": 627479,
"Highland, United Kingdom": 235540,
"Lanarkshire, United Kingdom": 319020,
"London, United Kingdom": 8982000,
"Lothian, United Kingdom": 858090,
"Midlands, United Kingdom": 2646000,
"North East and Yorkshire, United Kingdom": 2700000,
"North West, United Kingdom": 7300000,
"Northern Ireland, United Kingdom": 1885000,
"Orkney, United Kingdom": 22055,
"Scotland, United Kingdom": 5454000,
"Shetland, United Kingdom": 22990,
"South East, United Kingdom": 9175000,
"South West, United Kingdom": 5616000,
"Tayside, United Kingdom": 416090,
"Wales, United Kingdom": 3136000,
"Abruzzo, Italy": 1312000,
"Basilicata, Italy": 562869,
"Bolzano, Italy": 106951,
"Calabria, Italy": 1947000,
"Campania, Italy": 5802000,
"Emilia-Romagna, Italy": 4459000,
"Friuli Venezia Giulia, Italy": 1215000,
"Lazio, Italy": 5879000,
"Liguria, Italy": 1551000,
"Lombardia, Italy": 10060000,
"Marche, Italy": 1525000,
"Molise, Italy": 308493,
"Piemonte, Italy": 4269714,
"Puglia, Italy": 4029000,
"Sardegna, Italy": 1640000,
"Sicilia, Italy": 5000000,
"Toscana, Italy":  3730000,
"Trento, Italy": 117417,
"Umbria, Italy": 882015,
"Valle d'Aosta, Italy": 125666,
     "Veneto, Italy": 4906000,"Luxembourg, Luxembourg": 632275,"Burgenland, Austria": 293433,
"Kärnten, Austria": 560939,
"Niederösterreich, Austria": 1678000,
"Oberösterreich, Austria": 1482000,
"Salzburg, Austria": 152367,
"Steiermark, Austria": 1243000,
"Tirol, Austria": 754705,
"Vorarlberg, Austria": 394297,
     "Wien, Austria": 1897000,
     "Montenegro, Montenegro": 621718,
"Vâlcea, Romania": 92573,
"Alba, Romania": ,
"Arad, Romania": ,
"Argeș, Romania": ,
"Bacău, Romania": ,
"Bihor, Romania": ,
"Bistrița-Năsăud, Romania": ,
"Botoșani, Romania": ,
"Brașov, Romania": ,
"Brăila, Romania": ,
"București, Romania": ,
"Buzău, Romania": ,
"Caraș-Severin, Romania": ,
"Cluj, Romania": ,
"Costanza, Romania": ,
"Covasna, Romania": ,
"Călărași, Romania": ,
"Dolj, Romania": ,
"Dâmbovița, Romania": ,
"Galați, Romania": ,
"Giurgiu, Romania": ,
"Gorj, Romania": ,
"Harghita, Romania": ,
"Hunedoara, Romania": ,
"Ialomița, Romania": ,
"Iași, Romania": ,
"Ilfov, Romania": ,
"Maramureș, Romania": ,
"Mehedinți, Romania": ,
"Mureș, Romania": ,
"Neamț, Romania": ,
"Olt, Romania": ,
"Prahova, Romania": ,
"Satu Mare, Romania": ,
"Sibiu, Romania": ,
"Suceava, Romania": ,
"Sălaj, Romania": ,
"Teleorman, Romania": ,
"Timiș, Romania": ,
"Tulcea, Romania": ,
"Vaslui, Romania": ,
"Vrancea, Romania": ,
"Vâlcea, Romania": ,
"Agder, Norway": ,
"Innlandet, Norway": ,
"Møre og Romsdal, Norway": ,
"Nordland, Norway": ,
"Oslo, Norway": ,
"Outside mainland Norway": ,
"Rogaland, Norway": ,
"Troms og Finnmark, Norway": ,
"Trøndelag, Norway": ,
"Vestfold og Telemark, Norway": ,
"Vestland, Norway": ,
"Viken, Norway": ,
"Ahvenanmaa, Finland": ,
"Etelä-Karjala, Finland": ,
"Etelä-Pohjanmaa, Finland": ,
"Etelä-Savo, Finland": ,
"HUS, Finland": ,
"Itä-Savo, Finland": ,
"Kainuu, Finland": ,
"Kanta-Häme, Finland": ,
"Keski-Pohjanmaa, Finland": ,
"Keski-Suomi, Finland": ,
"Kymenlaakso, Finland": ,
"Lappi, Finland": ,
"Länsi-Pohja, Finland": ,
"Pirkanmaa, Finland": ,
"Pohjois-Karjala, Finland": ,
"Pohjois-Pohjanmaa, Finland": ,
"Pohjois-Savo, Finland": ,
"Päijät-Häme, Finland": ,
"Satakunta, Finland": ,
"Vaasa, Finland": ,
"Varsinais-Suomi, Finland": ,
"West North, Finland": }

'''
{"Aargau, Switzerland":678207, "Zug, Switzerland":29804, "Uri, Switzerland":36433,"Jura, Switzerland":73419, "Graubünden, Switzerland":198379, "Vaud, Switzerland":799145, "Thurgau, Switzerland":282909, "Ticino, Switzerland":350986, "St. Gallen, Switzerland": 75481, "Uri, Switzerland":60439692,
      'Solothurn, Switzerland':16163, '':7451955, '':13606320,
      'Jharkhand':38471, 'Karnataka':67562686, 'Kerala':35699443, 'Ladakh':274289,
      'Lakshadweep':64473, 'Madhya Pradesh':85047748, 'Maharashtra':
112374333, 'Manipur':2855794, 'Meghalaya':3366710, 'Mizoram':1239244, 'Nagaland':1980602,
      'Odisha':47645822, 'Puducherry':877010, 'Punjab':30141373, 'Rajasthan':81032689,
      'Sikkim':619000, 'Tamil Nadu':77841267, 'Telangana':38510982, 'Tripura':4071,
      'Uttar Pradesh':237882725, 'Uttarakhand':11250858, 'West Bengal':100580953, "Delhi":31181000}
'''
#np.seterr('raise')
def linear_fit(x, a, b):
    return  a*x+b


def make_big_plot(item0, df7):
    #print(item0)
    state = item0 # can choose any state from df.Region.unique()                                                                                                      
    threshold = 1 # x cases per million population                                                                                                                   
    offset_days = 60 # keep the most recent 60 days                                                                                                                  
    days = [(45,60)] # the time window to fit the decline curve, 45-60 usually works (60 is the most recent date)                                                    
    try:
        focus = df7.set_index('date', drop=True)#.drop(['cases0'], axis=1)
        focus.index = pd.to_datetime(focus.index).strftime('%Y-%m-%d')
        focus = focus['cases'].diff()[-offset_days:]
        title = state
        fig, ax = plt.subplots(nrows=1, ncols=1, sharey=True, figsize=(16,9))
        ax.plot(focus.index, focus.values, alpha=0.3)#, label=r'Daily cases in %s'%title)                                                                          
        ax.plot(focus.rolling(window=7, min_periods=1, center=True).mean(), c='green',alpha=0.3, ls='--')
        for i,(a,b) in enumerate(days):
            slope, intercept = optimize.curve_fit(linear_fit, np.arange(a,b), np.log(focus.values[a:b]+1))[0]
            ax.plot(np.arange(a,b), np.exp(np.arange(a,b)*slope + intercept), c=('C'+str(i+1)))
            ax.annotate(np.round(np.exp(slope),3), xy=((a+b-2)/2, np.exp((a+b+2)/2*slope + intercept)), fontsize=24, c=('C'+str(i+1)))
        
        ax.set_yscale('log') #turn on/off this line to use log or linear scale        
        b = np.array([focus.values[-1]], dtype=numpy.float64)#"Schaffhausen, Switzerland"
        #if state not in ["Emilia-Romagna, Italy","Campania, Italy","Calabria, Italy","Bolzano, Italy","Basilicata, Italy","Abruzzo, Italy","South West, United Kingdom","South East, United Kingdom","Northern Ireland, United Kingdom","North West, United Kingdom","North East and Yorkshire, United Kingdom", "Solothurn, Switzerland","Obwalden, Switzerland","Uri, Switzerland","Ticino, Switzerland","East of England, United Kingdom","London, United Kingdom","Midlands, United Kingdom","Scotland, United Kingdom"]:        
        while b[-1] > pop[state] / 1e6 * threshold:
            try:
                b = np.append(b, b[-1]*(1+slope))
            except Exception:
                pass
        try:    
            numdays=len(b)+10
            base = datetime.date.today()
            date_list = list(focus.index)+[(base + datetime.timedelta(days=x)).strftime('%Y-%m-%d')  for x in range(0+numdays)]
            ax.plot(date_list,[pop[state]/1e6* threshold for x in range(0,len(date_list))],'--', label=str(threshold)+'/Mppl', linewidth=2)
            ax.plot(np.arange(len(focus),len(focus)+len(b)), b, ls='-.', c='C4')
        except:
            pass
        ax.legend(prop={'size': 30})
        #except  Exception:
        #    #print("An exception occurred")
        #    pass
        ax.tick_params(labelsize=20)
        ax.xaxis.set_major_locator(plt.MaxNLocator(8))
        ax.set_ylim(bottom=1, )
        try:
            ax.annotate(s=str(len(b))+' days until \ndaily cases\n<'+str(threshold)+' /Mppl', xy=(len(focus)+len(b)-9, 20), fontsize=20, ha='center', c='C4')#len(focus)+len(b)-9                                                                                                                         
        except:
            print(str(len(b))+' days until \ndaily cases\n<'+str(threshold)+' /Mppl')
            #continue
        
        plt.title(state, fontsize=20)
        plt.tight_layout()
        #plt.show()
        
        plt.savefig(output_directory + '/classification/'+state+'_1.png')
        
        plt.close()
    except:
        print(item0)
        #continue           
    return item0





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

for kkey in list(all_countries.keys()):
    df3=all_countries[kkey]
    print(df3)
    #.dropna().groupby(["DATE","PROVINCE","REGION"])["CASES"].sum().reset_index()
    df3["Combined_Key"]=df3["Region"]+", "+df3["CountryName"]
    df4=pd.pivot_table(df3, values='CumulativePositive', index=['Combined_Key'],columns=['Date'],aggfunc=np.sum)
    #print(df4)
    output_directory = 'output_'+kkey.lower()
    os.makedirs(output_directory + '/classification', exist_ok=True)
    #print(output_directory)
    e_dataframe = df3.set_index("iso3")
    ids = df3[["Combined_Key"]].to_dict('records')
    recs = df3["Combined_Key"].to_list()
    e_dataframe1 = df4
    e_dataframe0=e_dataframe1.transpose()
    #print(e_dataframe0)
    add_day_columns(e_dataframe0)
    tim = list(df4.columns)
    tim.pop(0)
    
    #print("time")
    #print(tim[80:])
    ind4 = 0
    aar = []
    aar1 = []
    counties = e_dataframe0.columns[3:]
    #print("counties")
    #print(counties)
    
    for name in counties:
        values = e_dataframe0[name].fillna(0)
        #print(values)
        num_rows = len(values)
        y50 = values[-14:]
        y5 = [y - values[-14] for y in y50]
        y = values
        original_values = compute_original_values(values)
        x = e_dataframe1[e_dataframe1.columns[0]]
        y1 = interpolate(y)
        x2 = x[9:]
        tim2 = tim[4 : -5]
        y3 = pd.DataFrame(y1, columns=["a"]).rolling(window=10).mean()['a'].to_list()[9:]
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

            print(name,color,ratio,recent_mean0,int(max(y5)))    
            with open(output_directory + '/classification/data_counties_'+str(ids[recs.index(name)]["Combined_Key"]).split(", ")[0]+'.json', 'w') as outfile:
                json.dump({"dates":tim2,"max_14": int(max(y5)-min(y5)),"max":int(max(y)),"value":y3,"time":tim,"original_values":original_values},outfile)
                #print(tim2)
                #print(tim)
                #print(original_values)
                tt=[20 for x in range(0,len(tim))]
                #fig, ax = plt.subplots(nrows=1, ncols=1, sharey=True, figsize=(16,9))
                dda=pd.DataFrame(tim, columns=["date"])
                dda["date"]=pd.to_datetime(dda["date"], format='%Y-%m-%d')
                #print(original_values)
                dda["cases0"]=original_values
                dda["cases"]=dda["cases0"].cumsum()
                dda=dda.drop(['cases0'], axis=1)
                #print(name,dda)
                make_big_plot(name, dda)
                
                fig, ax = plt.subplots(nrows=1, ncols=1, sharey=True, figsize=(16,9)) 
                ax.plot(dda["date"],tt)
                ax.plot(dda["date"],original_values,c='C4')
                ax.tick_params(labelsize=12)
                ax.xaxis.set_major_locator(plt.MaxNLocator(8))
                plt.title(name, fontsize=12)
                plt.tight_layout()
                plt.savefig(output_directory + '/classification/'+str(ids[recs.index(name)]["Combined_Key"]).split(", ")[0]+"_3.png", dpi=150)
                #plt.show()
                plt.close()
                
                #make_big_plot(name, dda) 
            #aar.append({"color":color,"province":name.split(",")[0],"country":name.split(",")[1],"id":"new_id_"+str(ind4),"value1":ratio, "dates":tim2,"value":y3})
            aar1.append({"n":name.split(", ")[0],"id":ids[recs.index(name)]["Combined_Key"].split(", ")[0],"v":ratio,"c":color,"max":int(max(y5)-min(y5))})
            ind4+=1
    aar1[0]["date"]=date_of_analysis
    # this file is used by the map
    with open(output_directory + '/classification/classification_ids_counties2.json', 'w') as outfile:
        json.dump(aar1, outfile)


