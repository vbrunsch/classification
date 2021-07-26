import schedule
import time
import os
'''
def job(t):
    print("I'm working...", t)
    return

schedule.every().day.at("18:45").do(job,'It is 19:00')

while True:
    schedule.run_pending()
'''
#os.system("rm -r /Users/olgabuchel/Downloads/archive")
#wget https://www.kaggle.com/lisphilar/covid19-dataset-in-japan/download

os.system("pythonw process_japan.py")
os.system("python3 prepare_greece_prefactures.py")
os.system("pythonw /Users/olgabuchel/downloads/decksample/directory/COVID-19_map_final/jhu_fixed.py")
os.system("pythonw prepare_classification_counties_final_ireland.py")
os.system("pythonw prepare_classification_counties_final_ireland1.py")
os.system("print('ireland')")
os.system("pythonw prepare_classification_counties_final_new.py")
os.system("print('us')")

#os.system("python3 prepare_classification_counties_argentina.py")
#os.system("print('argentina')")

os.system("pythonw prepare_classification_counties_arizona.py")
os.system("print('arizona')")

os.system("pythonw prepare_classification_counties_final_germany_new.py")
os.system("pythonw prepare_classification_counties_final_germany_new1.py")
os.system("print('germany')")

os.system("pythonw prepare_classification_counties_final_netherlands_new.py")
os.system("pythonw prepare_classification_counties_final_netherlands_new1.py")
os.system("print('netherlands')")
os.system("pythonw prepare_classification_counties_final_portugal1.py")
os.system("print('portugal')")
os.system("pythonw prepare_classification_counties_final_spain.py")
os.system("pythonw prepare_classification_counties_final_spain1.py")
os.system("print('spain')")
os.system("pythonw europe.py")
os.system("pythonw europe1.py")
os.system("print('europe')")
os.system("pythonw france.py")
os.system("pythonw france1.py")
os.system("print('france')")
os.system("pythonw belgium.py")
os.system("pythonw belgium1.py")
os.system("print('belgium')")
os.system("pythonw prepare_classification_counties_sweden.py")
os.system("print('sweden')")
#curl -d '%7B%22resource_id%22%3A%228a21d39d-91e3-40db-aca1-f73f7ab1df69%22%2C%22q%22%3A%22%22%2C%22filters%22%3A%7B%7D%2C%22include_total%22%3Atrue%2C%22limit%22%3A78120%2C%22offset%22%3A0%7D' https://data.gov.il/api/3/action/datastore_search -o israel_data_today.json 
os.system("pythonw prepare_israel_data.py")
os.system("pythonw process_israel_15.py")
os.system("pythonw process_israel_15_group.py")
os.system("print('israel')")
os.system("pythonw fire_plots.py")
os.system("pythonw fire_plots.py")
os.system("pythonw fire_plots_india.py")
os.system("pythonw fire_plots_poland.py")
os.system("pythonw fire_plots_russia.py")
'''
#    time.sleep(60) # wait one minute
os.system("pythonw fire_plots_us_ra.py")
os.system("pythonw fire_plots_us.py")
os.system("pythonw fire_plots.py")
os.system("pythonw fire_plots_us_cum.py")
#nohup python2.7 MyScheduledProgram.py &    
#git reset --hard HEAD~2
'''
