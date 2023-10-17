#First get the JSON response 

import requests
url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/2023-01-09?adjusted=true&apiKey=oyer6IDWlSr1WINc4waUeeRckoJG7Hsk"
response = requests.get(url)

#Second parse the JSON response using response.json() method
jsonResponse = response.json()

#print the entire response
#print ("Entire JSON response")
#print (jsonResponse)

#print specific keys and their values individually in jsonResponse
print ("Printing JSON response in Key:Value Pairs")
print (jsonResponse.items())

#print select key value pairs only
