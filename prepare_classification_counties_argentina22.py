import pandas as pd

data=pd.read_csv("/Users/olgabuchel/Downloads/Covid19Casos.zip",compression="zip")
print(data)
print(data.columns)
