import random

print("What is my magic number (1 to 100) ?")
mynumber = random.randint(1, 100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynumber:
    yourguess = int(input("Enter your guess: "))
    if yourguess < mynumber:
        print(" too low")
    elif yourguess > mynumber:
        print("too high")
    ntries += 1

if yourguess == mynumber:
    print("Yes! it's", mynumber)
else:
    print("Sorry! my number is", mynumber)