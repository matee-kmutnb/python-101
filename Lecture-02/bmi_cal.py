weight = int(input('Enter your weight in kilograms: '))
height = float(input('Enter your height in meters: '))

BMI = weight / (height ** 2)
print('Your BMI is: ' ,format(BMI , '.2f'))