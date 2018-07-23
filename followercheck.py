# Imports
import tweepy
import time
import random
from config import consumer_key_3, consumer_secret_3, access_token_3, access_token_secret_3
# uses snakeresearcher2

# Authorizations for tweepy
auth = tweepy.AppAuthHandler(consumer_key_3, consumer_secret_3)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

Prelim = open("TextFiles/prelim.txt", "r").readlines()


#Prelim = open("prelim.txt", "r").readlines()
def one_follower_check(name):
    person = api.get_user(name)
    if(person.followers_count > 50):
        # print("User has less than 150 followers")
        # print(person.screen_name + " has " + str(person.followers_count) + " followers.")
        if (already_followed(name)):           
            return False
        else:
            return True
    else:
        # print(person.screen_name + " has " + str(person.followers_count) + " followers (sufficient)")
        return False

def already_followed(name):
    with open("TextFiles/followed.txt", "r") as followedFile:
        if name in followedFile:
            # print(name + " is already followed")
            return True
        else:
            # print(name + " is new")
            return False


def write_one_follower(name):
    if(one_follower_check(name) == True):
        with open("TextFiles/filteredprelim.txt", "a") as temp:
            print("Writing " + name)
            temp.write(name)

def main():
    for user in Prelim:
        write_one_follower(user)
        # already_followed(user)

main()