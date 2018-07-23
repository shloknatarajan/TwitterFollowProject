# Imports
import tweepy
import time
import random
from config import consumer_key_skejul, consumer_secret_skejul, access_token_skejul, access_token_secret_skejul

# Authorizations for tweepy
auth = tweepy.OAuthHandler(consumer_key_skejul, consumer_secret_skejul)
auth.set_access_token(access_token_skejul, access_token_secret_skejul)
api = tweepy.API(auth)



def update_following():
    count = 0
    newusers = tweepy.Cursor(api.friends).items()
    oldusers = list(map(str.strip, open("TextFiles/following.txt").readlines()))
    newlist = []
    tracker = 0
    for newuser in newusers:
        count += 1
        if newuser.screen_name in oldusers:
            print("{} = old followed".format(newuser.screen_name))
            tracker += 1
            newlist.append(newuser.screen_name)
            if tracker > 1:
                break
        else:
            print("{} = new followed".format(newuser.screen_name))
            newlist.append(newuser.screen_name)
        if count > 10: # fall back to not overload twitter api calls
           break
    
    list_to_doc(newlist, oldusers)

def list_to_doc(newlist, oldusers):
    for i in newlist:
        if i in oldusers:
            oldusers.remove(i)

    for i in reversed(newlist):
        oldusers.append(i)

    open("TextFiles/following.txt", "w").close()
    for i in oldusers:
        with open("TextFiles/following.txt", "a") as followerFile:
                followerFile.write(i + "\n")
                print("Writing " + i)

def main():
    update_following()

main()
