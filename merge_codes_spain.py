import pandas as pd
import json

data0=pd.read_csv("iso_codes_spain.csv")
print(data0)
kkeys={}
for item in data0.iterrows():
    print(item[1])
    if item[1]["Subdivision name "].split(" [")[0][len(item[1]["Subdivision name "].split(" [")[0])-1:]==" ":
        kkeys[item[1]["Subdivision name "].split(" [")[0][:-1]]=item[1]["3166-2 code "]
    else:
        kkeys[item[1]["Subdivision name "].split(" [")[0]]=item[1]["3166-2 code "]
print(kkeys)
with open("ESP_adm2-1.json","r") as fileopen:
    data=json.load(fileopen)
    for item in data["features"]:
        if item["properties"]["NAME_2"]=="Baleares":
            item["properties"]["NAME_2"]="Balears"
        #Bizkaia Vizcaya
        if item["properties"]["NAME_2"]=="Vizcaya":
            item["properties"]["NAME_2"]="Bizkaia"
        #guipuzcoa pais vasco
        if item["properties"]["NAME_2"]=="Guipúzcoa":
            item["properties"]["NAME_2"]="País Vasco"
        if item["properties"]["NAME_2"] in list(kkeys.keys()):
            print("yes",item["properties"]["NAME_2"])
        else:
            print("no",item["properties"]["NAME_2"])
        item["properties"]["province_iso"]=kkeys[item["properties"]["NAME_2"]].split("-")[1].replace("*","").replace(" ","")
        print(item["properties"]["province_iso"])
    with open("ESP_adm2.json","w") as file_name:
        json.dump(data,file_name)
#print(data0["3166-2 code "].to_list())
