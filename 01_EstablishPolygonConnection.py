# This program will establish connection with Polygon using the generated API key
# Pass the API key in the following 'https' query - https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=oyer6IDWlSr1WINc4waUeeRckoJG7Hsk

# First question that comes up is how do you pass http
# Step 1: Import Requests
# Step 2: Use the GET command to connect to the API URL
# Step 3: Print the response 

import requests
response = requests.get('https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=oyer6IDWlSr1WINc4waUeeRckoJG7Hsk')
print(response.status_code)
