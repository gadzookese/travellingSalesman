#Felipe Pazos
#4//7/2016
#
#File for containing resources methods.
#

from math import sqrt, atan, atan2, pi, radians, sin, cos
import sys
import random

def write( image, fileName ):
    print("writing to: ", fileName)
    f = open( fileName, 'w')

    vals = []

    width = len(image[0])
    height = len(image)

    print(width, height) 

    f.write("P3 \n")
    f.write( str( width )+" "+ str(height) + "\n" )
    f.write( str(255) +"\n")

    f.write( "\n" )

    for line in image:
        for pixel in line:
            for val in pixel:
                f.write( str(val) + " ")
        
        f.write( "\n" )

    f.close()

def graphArray( arr ):
    maxVal = -1 * sys.maxsize
    minVal = sys.maxsize

    width = len( arr )
    height = width 

    for val in arr:
        maxVal = max( maxVal, val )
        minVal = min( minVal, val )

    newPixels = []

    #Make blank image.
    for r in range( height + 1 ):
        newPixels.append( [] )
        for c in range( width ):
            newPixels[r].append( (0, 0, 0) )

    for c in range( width ):
        y = 1  
        if maxVal != minVal:
            y = int( (arr[c]-minVal) / (maxVal-minVal) * height )   
        newPixels[height - y][c] = (255, 255, 255)

    return newPixels

def overlay( pixels1 , pixels2 ):

    width = len( pixels1[0] )
    height = len( pixels1 )

    newPixels = []

    for r in range( height ):
        newPixels.append( [] )

        for c in range( width ):
            newPixels[r].append( (pixels1[r][c][0], pixels2[r][c][0], 0 ) )


    return newPixels



def createImage( cities, filename ):

    minX = cities[0][0]
    maxX = cities[0][0]

    minY = cities[0][1]
    maxY = cities[0][1]

    for city in cities:

        print( city )
        minX = min( city[0], minX )
        maxX = max( city[0], maxX )

        minY = min( city[1], minY )
        maxY = max( city[1], maxY )

    image = []

    for r in range(320):
        image.append( [] )
        for c in range(320):
            image[r].append( (255,255,255) )


    for i in range( len( cities ) ):

        currCity = cities[i]
        nextCity = cities[(i+1)%(len(cities)) ]

        currX = 10 + 300*(currCity[0] - minX)/( maxX - minX ) 
        currY = 10 + 300*(currCity[1] - minY)/( maxY - minY ) 

        nextX = 10 + 300*(nextCity[0] - minX)/( maxX - minX ) 
        nextY = 10 + 300*(nextCity[1] - minY)/( maxY - minY ) 

        dx = nextX - currX
        dy = nextY - currY
        mag = sqrt( dx*dx + dy*dy )

        dx = dx/mag
        dy = dy/mag

        travelX = currX
        travelY = currY
        
        while sqrt( (travelX - nextX)**2 + (travelY - nextY)**2 ) > 1:
            print( (travelX - nextX, travelY - nextY) )
            image[320 - int(travelX)][int(travelY)] = (0, 0, 0)

            travelX += dx
            travelY += dy

        for dx in range( -1, 2 ):
            for dy in range( -1, 2 ):
                image[320 - int(currX+dx)][int(currY+dy)] = (255, 0, 0)
                image[320 - int(nextX+dx)][int(nextY+dy)] = (255, 0, 0)
    write( image, filename)