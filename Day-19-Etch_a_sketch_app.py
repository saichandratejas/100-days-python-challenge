# Rules are :
  '''  "w" to move forward
       "s" to move backwards
       "a" to move counter clock-wise
       "d" to move clock-wise
       "c" to clear the screen '''

from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forwards():
  tim.forward(10)
  
def move_backwards():
  tim.backward(10)
  
def counter_clockwise():
  new_heading=tim.heading()+10
  tim.setheading(new_heading)
  
def clockwise():
  new_heading=tim.heading()-10
  tim.setheading(new_heading)

def clear():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()
