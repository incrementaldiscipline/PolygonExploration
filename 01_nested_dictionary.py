import pandas as pd
import requests
import time 

#turning on the time counter
start_time = time.time()


url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/2023-01-09?adjusted=true&apiKey=oyer6IDWlSr1WINc4waUeeRckoJG7Hsk"
response = requests.get(url)
jsonResponse = response.json()

# just selecting the data from the results 
sample_nest = jsonResponse['results']
print (type(sample_nest[1]))
#method1
#df1 = pd.read_json(url)

#method2
#df2 = pd.DataFrame(jsonResponse)

#print (df1.head())

#printing total time taken to run the program
print(" --- %s seconds" %(time.time() - start_time))