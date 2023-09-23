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
choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor : "))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Invlid")
import random    
pack = [rock, paper, scissors]
comp_choice = random.choice(pack)
print(f"Computer choice :\n{comp_choice}")

if choice == 0 and comp_choice == pack[1]:
    print("You Lost")
elif choice == 1 and comp_choice == pack[0]:
    print("You Win")

elif choice == 1 and comp_choice == pack[2]:
    print("You Lost")
elif choice == 2 and comp_choice == pack[1]:
    print("You Win")
    
elif choice == 2 and comp_choice == pack[0]:
    print("You Lost")
elif choice == 3 and comp_choice == pack[2]:
    print("You Win")
    
elif choice == 0 and comp_choice == pack[2]:
    print("You Win")
    
elif choice >= 3 or choice < 0:
    print("Invlid")

else:
    print("Draw")

