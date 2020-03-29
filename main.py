#!/usr/bin/env python3

import requests
import json
import pandas as pd
                    
API_URL = 'https://pomber.github.io/covid19/timeseries.json'

response = requests.get(API_URL)
country = 'Sweden'
country_data = response.json()[country] 
df = pd.DataFrame(response.json()[country]) 

print(df)           
df.plot(x='date', color='#000000', style=[':','--','-','s:']).get_figure().savefig('graph.png')
                    


def jprint(obj):    
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# jprint(country_data)
