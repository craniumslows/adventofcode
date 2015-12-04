#!/usr/bin/python
# External Includes

import getopt
import sys


# Function Definitions


def howMuchPaper(l, w, h):
    sideA, sideB, sideC = [l * w, w * h, h * l]
    sides = [sideA, sideB, sideC]
    x = min(int(s) for s in sides)
    presentNeeds = 2 * l * w + 2 * w * h + 2 * h * l
    sparePaper = x
    return presentNeeds + sparePaper


def howMuchRibbon(l, w, h):
    bowRibbon = l * w * h
    sideA, sideB, sideC = [l * w, w * h, h * l]
    sides = {sideA: [l, w], sideB: [w, h], sideC: [h, l]}
    shortestWrap = min(int(s) for s in sides.keys())
    boxRibbon = (2 * sides[shortestWrap][1]) + (2 * sides[shortestWrap][0])
    return bowRibbon + boxRibbon


# Main


def main(argv):
    totalPaper = 0
    totalRibbon = 0
    inputFile = ''
    requestType = 'paper'
    outputValue = 0
    try:
        opts, args = getopt.getopt(argv, "ht:i:", ["type=", "input="])
    except getopt.GetoptError:
        print 'dayofcode2.py -t <ribbon|paper>  -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'dayofcode2.py -t <ribbon|paper>  -i <inputfile>'
            sys.exit(0)
        elif opt in ("-i", "--input"):
            inputFile = arg
        elif opt in ("-t", "--type"):
            requestType = arg

    f = open(inputFile)
    for line in iter(f):
        l, w, h = line.split('x')
        totalRibbon += howMuchRibbon(int(l), int(w), int(h))
        totalPaper += howMuchPaper(int(l), int(w), int(h))
    f.close()
    if requestType in ("paper", "p"):
        outputValue = totalPaper
    elif requestType in ("ribbon", "r"):
        outputValue = totalRibbon
    print(outputValue)


if __name__ == "__main__":
    main(sys.argv[1:])
