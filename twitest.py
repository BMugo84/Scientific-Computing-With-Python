# configparser used to store apikeys

import tweepy
import configparser

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter'] ['api_key_secret']

access_token = config['twitter'] ['access_token']
access_token_secret = config['twitter'] ['access_token_secret']

# authenitaction

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet = "Testing Mike 1, 2!"

api.update_status(tweet)
