"""
Convex Hull Animation using Gift Wrapping Algorithm

This program visualizes the Gift Wrapping algorithm (Jarvis March) for computing the convex hull of a set of points. Users can interactively add or remove points, and the convex hull updates dynamically.

Features:
    - Left-click to add points.
    - Right-click to remove points.
    - The convex hull is displayed as a polygon enclosing the points.
"""

from tkinter import * # Import tkinter
import math
#import gift_wrapping
from GiftWrapping import getConvexHull
def add(event):
    points.append([event.x, event.y])
    repaint()
def remove(event):
    for [x, y] in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove([x, y])
            repaint()
def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5
def repaint():
    canvas.delete("point")
    if len(points) > 0:
        #call fuction
        H = getConvexHull(points) # call GiftWrapping getConvexHull
        #draw lines
        for i in range(len(H) - 1):
            canvas.create_line(H[i][0], H[i][1], H[i + 1][0], H[i + 1][1], fill="black", tags="convex_hull")
        # Connect the last and first points to close the convex hull
        canvas.create_line(H[-1][0], H[-1][1], H[0][0], H[0][1], fill="black", tags="convex_hull")
    
        canvas.create_polygon(H, fill = "gray", tags = "point")

    for [x, y] in points:
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tags = "point")


    
        
def displayInstructions():
    instructions = ["INSTRUCTIONS", "Add:", "Left Click", "Remove:", "Right Click"]
    x = 20
    y = 20
    canvas.create_rectangle(x, y, x + 160, y + 80)
    canvas.create_text(x + 10 + 40, y + 20, text = instructions[0], justify =
    CENTER)
    for i in range(1, len(instructions), 2):
        canvas.create_text(x + 10 + 40, y + 20 + (i + 1) * 10, text =
        instructions[i], justify = RIGHT)
        canvas.create_text(x + 80 + 40, y + 20 + (i + 1) * 10, text =
        instructions[i + 1], justify = RIGHT)
window = Tk() # Create a window
window.title("Convex Hull") # Set title
width = 500
height = 150
radius = 2
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()
# Create a 2-D list for storing points
points = []
displayInstructions()
canvas.bind("<Button-1>", add)
canvas.bind("<Button-3>", remove)
window.mainloop() # Create an event loop
