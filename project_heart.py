# Approach:

# Import Turtle
# Make Turtle Object
# Define a method to draw a curve with simple forward and left moves
# Define a method to draw the full heart and fill the red color in it
# Define a method to display some text by setting position
# Call all the methods in main section.

import turtle

tr = turtle.Turtle()

def curve():
    for i in range(200):
        tr.right(1)
        tr.forward(1)
        
def heart():
    
    tr.fillcolor("red")
    tr.begin_fill()
    
    tr.left(140)
    tr.forward(113)
    
    curve()
    tr.left(120)
    
    curve()
    
    tr.forward(112)
    
    tr.end_fill()
    
def text():
    
    tr.up()
    
    tr.setpos(-68 , 95)
    
    tr.down()
    
    tr.color("lightgreen")
    
    tr.write("AZAM'S HEART", font = ("italian", 14 , "bold"))
    
heart()

text ()

tr.hideturtle()