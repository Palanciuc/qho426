print("What is your name human?")
n = input()
print("How old are you (in years)?")
a =  input()
print("How tall are you (in meters)?")
h = float(input())
print("How much do you weigh (in kilograms)?")
w = int(input())
bmi = w / h**2
print(n,"you are",a,"years old and your bmi is",float(bmi))