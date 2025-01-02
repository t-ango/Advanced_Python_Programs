"""
Gift Wrapping Algorithm for Convex Hull (16.11)

This program implements the Gift Wrapping algorithm (Jarvis March) to compute the convex hull of a set of 2D points. The convex hull is the smallest convex boundary that encloses all points in a given set.

Functions:
    - getConvexHull(points): Computes the convex hull using the Gift Wrapping algorithm.
    - rightmost_lowest_point(points): Finds the rightmost lowest point in the set.
    - checkSide(x0, y0, x1, y1, x2, y2): Determines the relative position of a point to a line.

Usage:
    - Randomly generates 50 points within a 100x100 grid.
    - Computes and prints the convex hull for these points.
"""

import random

def getConvexHull(points):
    #step 1
    H = []
    h0 = rightmost_lowest_point(points)
    first_point = points[h0]
    current_point = first_point
    H.append(current_point)
    next_point = points[1]
    index = 2
    nextindex = -1

    #step 2
    while True:
        t0 = current_point
        t1 = next_point

        checking = points[index]
        t2 = checking
        
        check = checkSide(current_point[0], current_point[1], next_point[0], next_point[1], checking[0], checking[1])
        if check < 0:
            next_point = checking
            nextindex = index
        index += 1

        if index == len(points):
            if next_point == first_point:
                break
            index = 0
            H.append(next_point)
            current_point = next_point
            next_point = first_point

    return H


def rightmost_lowest_point (points):
    index = 0
    for i in range(1,len(points)):
        if points[i][0] < points[index][0]:
            index = i
        elif points[i][0] == points[index][0]:
            if points[i][1] > points[index][1]:
                index = i
    return index

def checkSide(x0, y0, x1, y1, x2, y2):
    # <= 0 on the right side
    # > 0 on the left side
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

def main ():
    #input_points = input("Enter coordinates: ")
    #c = input_points.split()
    #points = [[float(c[i]), float(c[i + 1])] for i in range(0, len(c), 2)]

    points = []
    for i in range(50):
        x, y = random.random() *100, random.random() * 100
        points.append([x,y])

    convex_hull = getConvexHull(points)
    print (convex_hull)

main()


    