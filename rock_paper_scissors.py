from random import random
print("Welcome to Stone-Paper-Scissors")
list=["Stone","Paper","Scissors"]
random_num=int(random()*len(list))
score=0
comp=0
while(score<5 and comp<5):
  choice=int(input("0 for stone, 1 for paper, 2 for scissors: "))
  if choice==0 and random_num==2:
    print(list[random_num])
    score=score+1
    print("Great")
  elif choice==1 and random_num==0:
    print(list[random_num])
    score+=1
    print("Good Going")
  elif choice==2 and random_num==1:
    print(list[random_num])
    score+=1
    print("Nice")
  elif choice==random_num:
    print("Both Of you played it the same.")
  else:
    print(list[random_num])
    print("Ah! That Hurts.")
    comp=comp+1
  print("You=",score,"Computer=",comp,sep=" ")

if score>comp:
  print("You Won! Woohoo!")
else:
  print("Ah! You Lost.")