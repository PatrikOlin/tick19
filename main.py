#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(1, "./lib")

import requests
import json
import pandas as pd

import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont
                    
API_URL = 'https://pomber.github.io/covid19/timeseries.json'

response = requests.get(API_URL)
country = 'Sweden'
country_data = response.json()[country] 
df = pd.DataFrame(response.json()[country]) 
dead = '(x__x)'

# df.plot(x='date', color='#000000', style=[':','--','-','s:']).get_figure().savefig('graph.png')
                    
epd = epd2in13_V2.EPD()
epd.init()
print("Clear..")
epd.Clear(0xFF)

printToDisplay(dead)

def printToDisplay(string):
    HBlackImage = Image.new('1', (epd2in13_V2.EPD_HEIGHT, epd2in13_V2,EPD_WIDTH), 255)
         
    draw = ImageDraw.Draw(HBlackImage)

    draw.text((25, 65), string, fill = 0)

    epd.display(epd.getbuffer(HBlackImage))

def jprint(obj):    
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# jprint(country_data)
