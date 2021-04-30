'''Solve each of the following problem using python scripts. Make sure you see appropriate variable
names and comments . When there is a final answer have python print it to the screen.
A person's body mass index (BMI) is defined as:
BMI= mass in kg/(height in m)^2.'''

mass_of_person = int(input("Enter the mass of the person"))
height_of_person = int(input("Enter the height of the person"))
bmi = mass_of_person/(height_of_person)**2
print(f"A person's body mass index is {bmi}")