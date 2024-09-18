#TurtleGraphics.py
#Name: Brandon
#Date: 09/18
#Assignment: Turtle Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon(nano, sides):
    for s in range(sides):
        nano.forward(50)
        nano.right(360/sides)
    
def fillCorner(jesus, corner):
    #draw big square
    drawSquare(jesus, 100)
    
    if corner == 1:
        jesus.begin_fill()
        drawSquare(jesus, 50)
        jesus.end_fill()
    elif corner == 2:
        jesus.forward(50)
        jesus.begin_fill()
        drawSquare(jesus, 50)
        jesus.end_fill()
        
def squaresInSquares(zoro, num):
    zoro.penup()
    zoro.right(180)
    zoro.forward(120)
    zoro.right(90)
    zoro.forward(100)
    zoro.right(90)
    zoro.pendown()
    drawSquare(zoro, 240)
    zoro.penup()
    zoro.forward(20)
    zoro.right(90)
    zoro.forward(20)
    zoro.left(90)
    zoro.pendown()
    drawSquare(zoro, 200)
    zoro.penup()
    zoro.forward(20)
    zoro.right(90)
    zoro.forward(20)
    zoro.left(90)
    zoro.pendown()
    drawSquare(zoro, 160)
    zoro.penup()
    zoro.forward(20)
    zoro.right(90)
    zoro.forward(20)
    zoro.left(90)
    zoro.pendown()
    drawSquare(zoro, 120)
    zoro.penup()
    zoro.forward(20)
    zoro.right(90)
    zoro.forward(20)
    zoro.left(90)
    zoro.pendown()
    drawSquare(zoro, 80)
    
    
    





def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3)

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
