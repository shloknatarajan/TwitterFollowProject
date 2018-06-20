# Imports
import tweepy
import time
import random
from config import consumer_key_2, consumer_secret_2, access_token_2, access_token_secret_2
# uses snakeresearcher2

# Authorizations for tweepy
auth = tweepy.OAuthHandler(consumer_key_2, consumer_secret_2)
auth.set_access_token(access_token_2, access_token_secret_2)
api = tweepy.API(auth)

Prelim = open("TextFiles/prelim.txt", "r").readlines()

#Prelim = open("prelim.txt", "r").readlines()
def one_follower_check(name):
    person = api.get_user(name)
    if(person.followers_count > 150):
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
            temp.write(name)

def main():
    for user in Prelim:
        write_one_follower(user)
        # already_followed(user)
    print("Completed operation")

main()






        


        
