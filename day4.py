#!/usr/bin/python
# External Includes
import sys
import hashlib

# Function Definitions

def md5Check(inputVal,goalHeader):
    hashVal = hashlib.md5(inputVal).hexdigest()
    return (goalHeader != hashVal[0:(len(goalHeader))])

# Main

def main(argv):
    inputVal = argv[0]
    hCounter = 0

    while md5Check(inputVal + str(hCounter), '000000'):
        hCounter = int(hCounter) + 1

    print "The winning value is " + str(hCounter)

if __name__ == "__main__":
    main(sys.argv[1:]) # Chomp off the script name from argv
