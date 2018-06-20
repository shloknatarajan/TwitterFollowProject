def remove_duplicates():
    lines_seen = set()
    outfile = open("TextFiles/cleanedfiltered.txt", "w")
    for line in open("TextFiles/filteredprelim.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

def remove_followed():
    already_followed = open("TextFiles/followed.txt", "r").readlines()
    outfile = open("TextFiles/temp.txt", "w")
    for line in open("TextFiles/cleanedfiltered.txt", "r"):
        if line not in already_followed:
            outfile.write(line)
    outfile.close()

def copy_to_filtered():
    with open("TextFiles/temp.txt", "r") as inputFile:
        with open("TextFiles/filteredprelim.txt", "w") as outputFile:
            for line in inputFile:
                outputFile.write(line)
    

def main():
    remove_duplicates()
    print("Removed duplicates")
    remove_followed()
    print("Removed already followed")
    copy_to_filtered()
    print("Copied files")
    print("---Filter Cleaned---")
    

main()


