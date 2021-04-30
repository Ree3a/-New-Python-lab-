'''Write a program to find the am or pm from the time given by the user'''
time = int(input('Enter the time :'))
if time >= 12 :
    print("Its pm")
elif time <= 12:
    print("Its am ")
