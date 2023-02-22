import random

name = input('Whats your name?')
print('Hello', name.capitalize())

print('ok then')

while True:

    try:
        weight = float(input('Whats your weight in Kg?' ))

    except ValueError:
        print("Write a number dumbass")
        #better try again... Return to the start of the loop
        continue
    else:
        #weight was successfully parsed!
        #we're ready to exit the loop.
        break


while True:

    try:
        height = float(input('How tall are you in Cm?'))

    except ValueError:
        print("Numbers only dumbass")
        #better try again... Return to the start of the loop
        continue
    else:
        #height was successfully parsed!
        #we're ready to exit the loop.
        break

BMI = (weight)/((height)/100)**2
print('your BMI is', {BMI})

n= random.randint(1,365)
a= random.randint(1,24)
print('therefore your balls will explode in')
print('calculating......')
print(n,'days and',a,'hours')