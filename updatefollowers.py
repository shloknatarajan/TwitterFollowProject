# Imports
import tweepy
import time
import random
from config import consumer_key_4, consumer_secret_4, access_token_4, access_token_secret_4

# Authorizations for tweepy
auth = tweepy.OAuthHandler(consumer_key_4, consumer_secret_4)
auth.set_access_token(access_token_4, access_token_secret_4)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def update_followers():
    count = 0
    newusers = tweepy.Cursor(api.followers, screen_name="MLCobra", count = 50).items()
    oldusers = list(map(str.strip, open("TextFiles/followers.txt").readlines()))
    newlist = []
    tracker = 0 # tracker system works in case someone follows, unfollows, then follows back, making them appear in the old list
    for newuser in newusers:
        count += 1
        if newuser.screen_name in oldusers:
            print("{} is an old follower".format(newuser.screen_name))
            tracker += 1
            newlist.append(newuser.screen_name)
            if tracker > 1:
                break
        else:
            print("{} is a new follower".format(newuser.screen_name))
            newlist.append(newuser.screen_name)

        if count > 10: # fall back to not overload twitter api calls
           break

    list_to_doc(newlist, oldusers)


def list_to_doc(newlist, oldusers):

    newlist = list(map(str.strip, newlist))
    for i in newlist:
        if i in oldusers:
            oldusers.remove(i)

    for i in reversed(newlist):
        oldusers.insert(0, i)
    open("TextFiles/followers.txt", "w").close()
    for i in oldusers:
        with open("TextFiles/followers.txt", "a") as followerFile:
                followerFile.write(i + "\n")
                print("Writing " + i)

def main():
    update_followers()

try:
    main()
except Exception as e:
    print(e)
    print("Waiting for rate limit error to go away \n")
    time.sleep(15)  
