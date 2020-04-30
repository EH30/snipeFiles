import os
import sys
import argparse

#Created By: EH

def file_writer(filename, data):
    opn = open(filename, "a")
    opn.write(data+"\n")
    opn.close()


def getData(paths, name, multi):    
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
    

parser = argparse.ArgumentParser(description="Enter You're Path then the File Name")
parser.add_argument("path", type=str, help="Enter The Path To Search For Files")
parser.add_argument("filename", type=str, help="Enter The File Name To Search")
parser.add_argument("multi", type=str, help="This is to Search multiple Files With Same Name Enter y/n")
args = parser.parse_args()


if getData(args.path, args.filename, args.multi) == 1:
    print("[-]File Not Found")