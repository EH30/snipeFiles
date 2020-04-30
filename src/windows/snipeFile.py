import os
import sys


#Created By: EH

def file_writer(filename, data):
    opn = open(filename, "a")
    opn.write(data+"\n")
    opn.close()


def getData(paths, name, multi):
    if multi == "n" or multi == "y" or multi == "Y" or multi == "N":
        pass
    else:
        print("Enter y or n")
        exit()
    
    print("[+]Searching for: ", name)
    
    found = 0

    for root, dirname, filename in os.walk(paths):
        for x in filename:
            if x != []:
                if name == x:
                    file_writer("Found.txt", "[+]Found {0} in {1}".format(name, root))
                    print("[+]Found {0} in {1}".format(name, root))
                    found = 1
                    if multi == "y" or multi.upper() == "Y":
                        continue
                    
                    return 0

    if found != 0:
        return 0

    return 1
    

path = input("Enter Drive/Path (Example: C:\ ): ")
name = input("File Name: ")
multi = input("Search For Multiple File With The Same Name y/n: ").strip()

if getData(path, name, multi) == 1:
    print("[-]File Not Found")

os.system("pause")
