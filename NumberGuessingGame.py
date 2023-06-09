import random
#random no.
a = random.randint(0, 10)
#accepting input
print("Guess a number between 0 and 10: ")
while True:
    g = int(input())
    if g == a:
        print("Yes, you guessed it right!")
        break
    else:
        print("NO")
        continue