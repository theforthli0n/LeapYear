# leapYear.py written by Everett De Leon
# Goal: write a program that checks any year to see if it is a leap year.
# Last revised: 05/12/2021


# ask what year they want to check
year = int(input('What year would you like to check?'))


# order matters - logice math behind leap years
if year % 400 == 0:
    print(f'The year {year} is a leap year.')
elif year % 100 == 0:
    print(f'The year {year} is not a leap year.')
elif year % 4 == 0:
    print(f'The year {year} is a leap year.')
else:
    print(f'The year {year} is not a leap year.')
