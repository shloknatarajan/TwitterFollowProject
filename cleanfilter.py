def remove_duplicates():
    # Remove Duplicates
    lines_seen = set()
    noduplicates = []
    for line in open("TextFiles/filteredprelim.txt", "r"):
        if line.strip() not in lines_seen: # not a duplicate
            noduplicates.append(line.strip())
            lines_seen.add(line.strip())
    print("Removed duplicates")
    remove_followed(noduplicates)

def remove_followed(noduplicates):
    # Removing already followed users from list to follow
    already_followed = open("TextFiles/followed.txt", "r").readlines()
    already_followed = [x.strip() for x in already_followed]
    nofollowed = []
    for line in noduplicates:
        if line not in already_followed:
            nofollowed.append(line)
    print("Removed already followed")
    copy_to_filtered(nofollowed)

def copy_to_filtered(nofollowed):
    # Copy to filtered
    with open("TextFiles/filteredprelim.txt", "w") as final:
        for line in nofollowed:
            final.write("{}\n".format(line))
    print("Updated Original")



def main():
    remove_duplicates()

    print("---Filter Cleaned---")
    

main()

