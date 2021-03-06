# Imports
import tweepy
import time
import random
from config import consumer_key_1, consumer_secret_1, access_token_1, access_token_secret_1

# Authorizations for tweepy
auth = tweepy.AppAuthHandler(consumer_key_1, consumer_secret_1)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Methods
def follower_mine():
    users = tweepy.Cursor(api.followers, screen_name="MikeQuindazzi", count = 50).items()
    count = 0
    for user in users:
        
        # Writes to followed doc 
        with open("TextFiles/filteredprelim.txt", "a") as prelim:
            prelim.write(user.screen_name + "\n")
            print("Writing " + user.screen_name)
        count += 1

    print("Finished getting followers")

def main():
    follower_mine()

try:
    main()
except Exception:
    pass

