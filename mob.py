#!/usr/bin/python
#This program will read an txt file with multiple lines of ints.  It will use the first int in each line as the number of mobbers for the assigned problem.  The rest of the string will be used as x,y coordinates.  The program will find the best coordinate in the middle of all the given x,y coordinates.  The best coordinate means the least amount of distance traveled for each given x,y coordinate to get to the x,y point of the best coordinate found.  The program will also output the distance traveled for all the given x,y coordinates combined.  The program will end when it finds a 0 as the first integer in a string.

import os
import sys
import math
import time
inputFile = sys.argv[1]

#Iterate though the txt file. Call the sortLine(line) function to populate x and y arrays. Find the avgX and avgY coordinates.  Call the calculate function
def iterate(inputFile):
    with open(inputFile, 'r') as fileRead:
        output = fileRead.readlines()
        lineNumber = 0
        for line in output:
            if line.startswith("0"):
               break 

            #coordinates has X array at [0] and Y array at [1]
            coordinates = sortLine(line)
            lineNumber = calculate(coordinates, lineNumber)

def calculate(coordinates, lineNumber):
    mobbers = int(coordinates[2])    
    arrayX = coordinates[0]
    arrayY = coordinates[1]
    arrayX = sorted(arrayX)
    arrayY = sorted(arrayY)
    
    answer = 0
    i = 0
    for i in range(mobbers):
        answer += abs(arrayX[i] - arrayX[(mobbers - 1)/2])
        answer += abs(arrayY[i] - arrayY[(mobbers -1)/2])
    lineNumber += 1
    print "Line ", lineNumber, " : ", arrayX[(mobbers -1 ) /2], arrayY[(mobbers -1)/2], answer
    return lineNumber
            
#Populate X,Y coordinates into arrays
def sortLine(line):
    arrayX = []
    arrayY = []
    numOfMobbers = line.partition(' ')[ 0 ]
    restOfLine = line.split(' ',1)[1]
    x = map(int, restOfLine.split())
    for i in range(len(x)):
       if int(i) % 2 == 0:
            arrayY.append( x[i] )
       else:
            arrayX.append( x[i] )
    coordinates = []
    coordinates.append( arrayY )
    coordinates.append( arrayX )
    coordinates.append( numOfMobbers )
    return coordinates

#Main function.  Also figures out the run time of the program.
def main():
    start_time = time.time()    
    iterate(inputFile)
    print ("--- %s seconds ---" % (time.time() - start_time))
            
if __name__ == "__main__":
    main()
