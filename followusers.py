# Imports
import tweepy
import time
import random
from config import consumer_key_king, consumer_secret_king, access_token_king, access_token_secret_king

# Authorizations for tweepy
auth = tweepy.OAuthHandler(consumer_key_king, consumer_secret_king)
auth.set_access_token(access_token_king, access_token_secret_king)
api = tweepy.API(auth)

# Methods
def follow_from_file():
    toFollow = open("TextFiles/filteredprelim.txt", "r").readlines()
    count = 0 # keeps track of number of people followed per session
    for user in toFollow:
        person = api.get_user(user)
        # Checks if followed previously
        if(already_followed(user)):
            continue
        else:    
            with open("TextFiles/followed.txt", "a") as folowedFile:
                folowedFile.write(person.screen_name + "\n")
            print("Following " + person.screen_name)
            api.create_friendship(person.screen_name)
            count += 1 
            time.sleep(0.3 * random.randint(1, 10)) # Random pause (0.3 - 3 seconds)
            if (count > 50):
                print("Batch completed")
                break

def already_followed(name):
    with open("TextFiles/followed.txt", "r") as followedFile:
        if name in followedFile:
            # print(name + " is already followed")
            return True
        else:
            # print(name + " is new")
            return False

follow_from_file()