# Imports
import tweepy
import time
import random
from config import consumer_key_4, consumer_secret_4, access_token_4, access_token_secret_4

# Authorizations for tweepy
auth = tweepy.AppAuthHandler(consumer_key_4, consumer_secret_4)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Methods
def follower_mine():
    open("TextFiles/followers.txt", "w").close()
    users = tweepy.Cursor(api.followers, screen_name="SkejulME", count = 50).items()
    count = 0
    for user in users:
        
        # Writes to followed doc 
        with open("TextFiles/followers.txt", "a") as followers:
            followers.write(user.screen_name + "\n")
            print("Writing " + user.screen_name)
        count += 1


def main():
    follower_mine()

try:
    main()
except Exception:
    pass

