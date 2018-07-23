# Imports
import tweepy
import time
import random
from config import consumer_key_skejul, consumer_secret_skejul, access_token_skejul, access_token_secret_skejul

# This file does not use any twitter/tweepy calls
# Authorizations for tweepy
auth = tweepy.OAuthHandler(consumer_key_skejul, consumer_secret_skejul)
auth.set_access_token(access_token_skejul, access_token_secret_skejul)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def update_followed():
    count = 0
    newusers = list(map(str.strip, open("TextFiles/following.txt").readlines()))
    oldusers = list(map(str.strip, open("TextFiles/followed.txt").readlines()))
    newlist = []

    for newuser in newusers:
        if newuser in oldusers:
            print("{} has been followed before".format(newuser))
        else:
            print("{} has not been followed before".format(newuser))
            newlist.append(newuser)
            count += 1
    print("{} New Members added to followed.txt".format(count))
    list_to_doc(newlist, oldusers)

def list_to_doc(newlist, oldusers):
    for i in newlist:
        if i in oldusers:
            oldusers.remove(i)

    for i in newlist:
        oldusers.append(i)

    open("TextFiles/followed.txt", "w").close()
    for i in oldusers:
        with open("TextFiles/followed.txt", "a") as followerFile:
                followerFile.write(i + "\n")
                print("Writing " + i)
        

def main():
    update_followed()

main()
