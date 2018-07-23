# Imports
import tweepy
import time
import random
#from config import consumer_key_1, consumer_secret_1, access_token_1, access_token_secret_1
from config import consumer_key_skejul, consumer_secret_skejul, access_token_skejul, access_token_secret_skejul

# Authorizations for tweepy
auth = tweepy.OAuthHandler(consumer_key_skejul, consumer_secret_skejul)
auth.set_access_token(access_token_skejul, access_token_secret_skejul)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Uses followers and following files to compile non followers list, no API calls used
def get_non_followers():
    open("TextFiles/nonfollowers.txt", "w").close() # Clears nonfollowers file   
    count = 0	
    unfollow = []
    following = open("TextFiles/following.txt", "r").readlines()
    following = [x.strip() for x in following] # Removes \n characters at end
    # Following is listed from oldest to newest, so the oldest nonfollowers are listed first in nonfollowers.txt
        
    followers = open("TextFiles/followers.txt", "r").readlines()
    followers = [x.strip() for x in followers]

    for i in following:
        if i not in followers:
            unfollow.append(i)

    for user in unfollow:
        with open("TextFiles/nonfollowers.txt", "a") as nonfollowers:
            nonfollowers.write("{}\n".format(user))
            count += 1

    print("Found {} nonfollowers".format(count))

def remove_friendship():
    unfollowed = []
    count = 0
    toRemove = list(map(str.strip, open("TextFiles/nonfollowers.txt", "r").readlines()))
    for user in toRemove:
        api.destroy_friendship(user)
        count += 1
        print("Unfollowed {}".format(user))
        print("Count: {}".format(count))
        unfollowed.append(user)

        # Random pauses
        time.sleep(0.2 * random.randint(1, 10)) # 0.2 - 2 seconds in between each follow
        if (count % 200 == 0):
            print("200 completed. waiting random number of seconds (280-400 seconds)")
            time.sleep(40 *random.randint(7, 10))
            continue

        if count > 500:
            return unfollowed
    return unfollowed
        

def remove_from_following(unfollowed):
    print("Unfollowed: ")
    print(unfollowed)
    following = list(map(str.strip, open("TextFiles/following.txt", "r").readlines()))
   
    for i in unfollowed:
        if i in following:
            following.remove(i)
   
    with open("TextFiles/following.txt", "w") as outfile:
        for user in following:
            outfile.write("{}\n".format(user))
    
def main():
    get_non_followers() # Gets initial list of nonfollowers
    unfollowed = remove_friendship() # Unfollows N number of people
    remove_from_following(unfollowed) # Removes unfollowed users from following list
    get_non_followers() # Updates nonfollowers list

for i in range(100):
    try:
        main()
        break
    except tweepy.TweepError as err:
        print(err)

        # Deletes the user creating the error from the list
        lines = open('TextFiles/nonfollowers.txt').readlines()
        with open('TextFiles/nonfollowers.txt', 'w') as outfile:
            outfile.writelines(lines[1:])
        
        continue

