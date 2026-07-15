math = int(input('Enter your score: '))
eng = int(input('Enter your score: '))
com = int(input('Enter your score: '))
avg = (math + eng + com)/3
print(f"The average score is: {avg}")
if avg > 95 :
    print("congrat")
    print("you have great average")
else :
    print("meh")