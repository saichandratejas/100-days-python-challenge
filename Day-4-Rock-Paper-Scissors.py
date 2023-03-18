My Solution : https://replit.com/@saichandratejas/rock-paper-scissors-start#main.py


import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
image=[rock,paper,scissors]

input_by_user=int(input("Enter your choice : 0 for 'Rock', 1 for 'Paper' , 2 for ' Scissors' "))
if input_by_user >= 3 or input_by_user<0:
  print("Invalid Input!")
else:
  print(f"You chose : {input_by_user}")
  
  print(image[input_by_user])
  
  computer_choice=rand_no=random.randint(0,2)
  
  print(f"Computer chose : {rand_no}")
  
  print(image[computer_choice])

  
  if input_by_user == 0 and computer_choice == 2:
    print("You Win!")
  elif input_by_user == 2 and computer_choice == 0:
    print("You Loose!")
  elif input_by_user > computer_choice:
    print("You Win!")
  elif computer_choice > input_by_user:
    print("Computer Wins!")
  elif computer_choice == input_by_user:
    print("Its a Draw!")
  else:
    print("Invalid Input!")
