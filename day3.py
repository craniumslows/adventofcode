#!/usr/bin/python
# External Includes
import getopt
import sys
from collections import Counter

# Function Definitions

def moveSanta(direction,position):
    if direction == '<':
        position['x'] -= 1
    elif direction == '>':
        position['x'] += 1
    elif direction == '^':
        position['y'] += 1
    elif direction == 'v':
        position['y'] -= 1

def trackSanta(position,history):
    uniqIndex = "x" + str(position['x']) +  "y" + str(position['y'])
    if uniqIndex in history:
        history[uniqIndex] += 1
    else:
        history[uniqIndex] = 1

# Main


def main(argv):
    inputFile = False
    useRobot = False
    SantaPosition = {'x':0,'y':0}
    RoboPosition = {'x':0,'y':0}
    SantaHistory = {}
    RoboHistory = {}


    try:
        opts, args = getopt.getopt(argv, "hi:", ["input="])
    except getopt.GetoptError:
        print 'day3.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'day3.py -i <inputfile>'
            sys.exit(0)
        elif opt in ("-i", "--input"):
            inputFile = arg

    try:
        f = open(inputFile)
    except TypeError:
        print 'Invalid Parameters. '
        print 'Usage: day3.py -i <inputfile>'
        sys.exit(2)


    with open(inputFile) as f:
        for line in f:
            for c in line:
                if useRobot:
                    moveSanta(c,RoboPosition)
                    trackSanta(RoboPosition,RoboHistory)
                    useRobot = False
                else:
                    moveSanta(c,SantaPosition)
                    trackSanta(SantaPosition,SantaHistory)
                    useRobot = True

                pass
    f.close()

    # Now we need to combine santa and robo-santa's histories to get both present counts and houe visits
    # Thanks to SO for the Counter answer
    # method info http://stackoverflow.com/questions/11011756/is-there-any-pythonic-way-to-combine-two-dicts-adding-values-for-keys-that-appe
    RoboHistory = Counter(RoboHistory)
    SantaHistory = Counter(SantaHistory)
    TotalHistory = RoboHistory + SantaHistory
    print len(SantaHistory), len(RoboHistory),len(TotalHistory)

if __name__ == "__main__":
    main(sys.argv[1:])
