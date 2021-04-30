''' Given the integer N - the number of minutes that is passed since midnight- how many hours and
minutes are displayed on the 24h digital clock ?
The number of program should print two numbers : the number of hours (between 0 and 23 ) and the number of
minutes (between 0 and 59)
eg , if N = 150 , then 150 minutes have been passed since midnight i.e now is 2:30 am So the program
should print 2:20'''

time_passed = int(input("Enter the time that passed since midnight:"))
hours= time_passed//60
minutes = time_passed%60
print(f'{hours}')
print(f'{minutes}')
print(f'Its {(hours)}:{ (minutes)} now')





