# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:43:06 2020

@author: saren
"""

''' For Twitter '''
import tweepy as tp

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

def twtAPI():
    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    return tp.API(auth)

''' For Facebook Messenger '''
from fbchat import Client

email = ''
password = ''

def fbc_Client():
    return Client(email, password)
