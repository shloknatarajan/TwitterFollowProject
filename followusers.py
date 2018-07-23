# Imports
import tweepy
import time
import random
import cleanfilter
from config import consumer_key_skejul, consumer_secret_skejul, access_token_skejul, access_token_secret_skejul

# Authorizations for tweepy
auth = tweepy.OAuthHandler(consumer_key_skejul, consumer_secret_skejul)
auth.set_access_token(access_token_skejul, access_token_secret_skejul)
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
            # Adds users to the following and followed files    
            with open("TextFiles/followed.txt", "a") as followedFile:
                followedFile.write(person.screen_name + "\n")
            with open("TextFiles/following.txt", "a") as followingFile:
                followingFile.write(person.screen_name + "\n")

            print("Following " + person.screen_name)
            api.create_friendship(person.screen_name)
            count += 1 

            # Random pauses
            time.sleep(0.2 * random.randint(1, 10)) # 0.2 - 2 seconds in between each follow
            if (count % 200 == 0):
                print("200 completed. waiting random number of seconds (280-400 seconds)")
                time.sleep(40 *random.randint(7, 10))
                continue
                
            if (count > 500): # Stop follow process after certain number of people are followed
                print("Followed 500")
                break


def already_followed(name):
    with open("TextFiles/followed.txt", "r") as followedFile:
        if name in followedFile:
            return True
        else:
            return False

for i in range(1000000):
    try:
        follow_from_file()
        break
    except tweepy.TweepError as err:
        cleanfilter.main()
        print(err)

        if err.args[0][0]['code'] == 161: # Checks if twitter follow limit is reached
            print("Ending follow process -- limit reached")
            break

        # Deletes the user creating the error from the list
        lines = open('TextFiles/filteredprelim.txt').readlines()
        with open('TextFiles/filteredprelim.txt', 'w') as filtered:
            filtered.writelines(lines[1:])
        

        continue

        