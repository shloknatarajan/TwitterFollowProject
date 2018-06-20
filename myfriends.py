# Imports
import tweepy
import time
import random
from config import consumer_key_king, consumer_secret_king, access_token_king, access_token_secret_king

# Authorizations for tweepy
auth = tweepy.OAuthHandler(consumer_key_king, consumer_secret_king)
auth.set_access_token(access_token_king, access_token_secret_king)
api = tweepy.API(auth)

def get_my_friends():
    f = open("TextFiles/friends.txt", "w")
    f.close()
    print("Getting friends\n")
    count = 0
    users = tweepy.Cursor(api.friends).items()
    for user in users:
        with open("TextFiles/friends.txt", "a") as friends:
            friends.write(user.screen_name + "\n")
            count += 1
            if (count % 100 == 0):
                break



# Code to run
try:
    get_my_friends()
except tweepy.RateLimitError:
    print("Waiting for rate limit error to go away \n")
    time.sleep(15 * 60)    