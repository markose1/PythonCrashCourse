4 % 3 #prints the remainder of 4/3, which is 1
5 % 3 #prints the remainder of 5/3, which is 2
6 % 3 #prints the remainder of 6/3, which is 0
7 % 3 #prints the remainder of 7/3, which is 1

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.')

