My Code : https://replit.com/@saichandratejas/higher-lower-start

Solution:

from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  account_name=account['name']
  account_description=account['description']
  account_country=account['country']
  return(f'{account_name} ,\tis a {account_description} ,\tfrom {account_country}.')

def check_answer(guess,a_followers,b_followers):
  if a_follower_count >b_follower_count:
    if guess=='a':
      return guess=='a'
  else:
    return guess=='b'
clear() 
print(logo)
score=0
game=True
account_b=random.choice(data)
while game:
  
  account_a=account_b
  account_b=random.choice(data)
  # if account_a==account_b:
  #   account_b=random.choice(data)
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
  
  guess=input("Who has more followers 'A' or 'B'?! ").lower()
  
  a_follower_count=account_a['follower_count']
  b_follower_count=account_b['follower_count']
  is_correct=check_answer(guess,a_follower_count,b_follower_count)


  if is_correct:
          score+=1
          print(f"You are right!, Current Score is {score}")
  else:
          game = False
          print(f"You are wrong!, Current Score is {score}")
