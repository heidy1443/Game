import requests
import json
import sys

try:
    if len(sys.argv)<2:
        sys.exit("Missing command-line argument ")
    
    elif sys.argv[1].isalpha() :
        sys.exit("Command-line argument is not a number")
    
    response= requests.get("http://rest.coincap.io/v3/assets/bitcoin?apiKey=55c8ee9ee2f6264b9881f6305b4dbb309b8c30bec1b7fb692b8b59193f44bf8e")
    
    #print(json.dumps(response.json(),indent=4))
    p=response.json()
    price=float(p["data"]["priceUsd"])
    amount=float(sys.argv[1])*price
    print(f"${amount:,.4f}")

    
except requests.RequestException:
    pass