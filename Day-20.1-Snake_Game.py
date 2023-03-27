# MY SOLUTION LINK : https://replit.com/@saichandratejas/Snake-Game#snake.py

main.py :
  
  from turtle import Turtle ,Screen
from snake import Snake
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("The Snake Game")
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

  
screen.exitonclick()


python.py :
  
  from turtle import Turtle
starting_positions=[(0,0),(-20,0),(-40,0)]
move_distance=20
Up=90
Down=270
Left=180
Right=0

class Snake:
  def __init__(self):
    self.segments=[]
    self.create_snake()
    self.head=self.segments[0]
  
  def create_snake(self):
    for position in starting_positions:
      new_position=Turtle("square")
      new_position.color("White")
      new_position.penup()
      new_position.goto(position)
      self.segments.append(new_position)

      
  def move(self):
    for seg_num in range(len(self.segments)-1,0,-1):
      new_x=self.segments[seg_num -1].xcor()
      new_y=self.segments[seg_num -1].ycor()
      self.segments[seg_num].goto(new_x,new_y)
    self.head.forward(move_distance)
      
  def up(self):
    if self.head.heading()!=Down:
        self.head.setheading(Up)

  def down(self):
    if self.head.heading()!=Up:
        self.head.setheading(Down)

  def left(self):
    if self.head.heading()!=Right:
        self.head.setheading(Left)

  def right(self):
    if self.head.heading()!=Left:
        self.head.setheading(Right)
    
    
