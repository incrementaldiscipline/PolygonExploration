import pandas as pd
import requests
import time 


start_time = time.time()
url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/2023-01-09?adjusted=true&apiKey=oyer6IDWlSr1WINc4waUeeRckoJG7Hsk"
response = requests.get(url)
jsonResponse = response.json()

#method1
df1 = pd.read_json(url)

#method2
df2 = pd.DataFrame(jsonResponse)

print (df1.head())
print(" --- %s seconds" %(time.time() - start_time))

# so from here what we will try and do is 