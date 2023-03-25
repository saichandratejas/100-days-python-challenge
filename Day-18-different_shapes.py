import turtle as t

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########


def draw_shape (side):
  angle=360/side
  for _ in range(side):
    tim.forward(100)
    tim.left(angle)

for shape_side in range(3,11):
  draw_shape(shape_side)
