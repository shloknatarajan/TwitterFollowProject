
def main():
    friends = open("TextFiles/friends.txt", "r").readlines()
    friends.reverse()
    with open("temp.txt", "w") as temp:
        for user in friends:
            temp.write(user)

main()
