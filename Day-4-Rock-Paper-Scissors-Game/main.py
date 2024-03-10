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
import random

input_list = [rock, paper, scissors]
your_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?\n"))
if your_input >= 3 or your_input < 0:
  print('You typed an invalid number')
else:
  
  print(input_list[your_input])
  
  
  computer_input = random.randint(0,2)
  
  print(f"Computer chose: {computer_input} {input_list[computer_input]} ")
  if (your_input == 2 and computer_input == 0) or (your_input == 1 and computer_input == 2) or (your_input == 0 and computer_input == 1): 
    print('You lose')
  elif (your_input == 0 and computer_input == 2) or (your_input == 2 and computer_input == 1) or (your_input == 1 and computer_input == 0):
    print('You win')
  elif your_input == computer_input:
    print("It's a draw!")
  elif your_input >= 3 or your_input < 0:
    print('You typed an invalid number')
    
  
