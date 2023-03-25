import turtle as t
import random

tim = t.Turtle()
color=['red','blue','green','yellow','orange','violet']
########### Challenge 4 - Random Walk ########
directions=[0,90,180,270]

for _ in range(90):
  tim.forward(10)
  tim.setheading(random.choice(directions))
  tim.color(random.choice(color))
