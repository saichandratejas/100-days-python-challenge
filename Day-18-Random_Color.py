######## Random Colour ############

import turtle as t
import random

t.colormode(255)
tim.speed("fastest")
tim = t.Turtle()
directions=[0,90,180,270]

def random_color():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  random_color=(r,g,b)
  return random_color

for _ in range(90):
  tim.forward(10)
  tim.color(random_color())
  tim.setheading(random.choice(directions))
