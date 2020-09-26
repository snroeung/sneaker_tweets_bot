# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:03:47 2020

@author: saren
"""

from config import twtAPI, fbc_Client 
import pandas as pd 
import re
import datetime
from fbchat.models import *

pd.set_option('display.max_colwidth', None)

id = 'sneakershouts'

api = twtAPI()
client = fbc_Client()

def getTweets(screen_name):
    tweets = pd.DataFrame(columns = ['text', 'day', 'time'])
    timeline = api.user_timeline(screen_name = screen_name, count = 100)
    today = datetime.date.today()
    today = today.strftime('%Y-%m-%d')
    
    for i in range(len(timeline)):
        txt = timeline[i].text
        date = timeline[i].created_at.strftime('%Y-%m-%d')
        time = timeline[i].created_at.strftime('%H:%M:%S')
        
        if re.search('^Release|^Dropping', txt):
            if date == today:
                tweets = tweets.append({'text': txt,
                                    'day': date,
                                    'time':time}, ignore_index=True)
        
        
    return tweets

twts = getTweets(id)

for i in range(len(twts)):
    client.send(Message(text=twts['text'][i]), thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()

