# Imports
import tweepy
import time
import random
from config import consumer_key_skejul, consumer_secret_skejul, access_token_skejul, access_token_secret_skejul

# Authorizations for tweepy
auth = tweepy.OAuthHandler(consumer_key_skejul, consumer_secret_skejul)
auth.set_access_token(access_token_skejul, access_token_secret_skejul)
api = tweepy.API(auth)

# Generates list in order from most recent to oldest sent follow
def get_my_following():
    open("TextFiles/following.txt", "w").close()
    print("Getting following\n")
    count = 0
    users = tweepy.Cursor(api.friends).items()
    for user in users:
        with open("TextFiles/following.txt", "a") as following:
            following.write(user.screen_name + "\n")
            count += 1

# Reverses list so it goes from oldest sent follow to most recent
def reverse_file():
    users = list(map(str.strip, open("TextFiles/following.txt").readlines()))
    users.reverse()
    open("TextFiles/following.txt", "w").close()
    for i in users:
        with open("TextFiles/following.txt", "a") as following:
            following.write(i + "\n")



# Code to run
try:
    get_my_following()
    reverse_file()
except tweepy.RateLimitError:
    print("Waiting for rate limit error to go away \n")
    time.sleep(15)    