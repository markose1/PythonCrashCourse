squares = [] #empty list
for value in range(1,11): #for every number between 1-10
    square = value**2 #square each number and store in variable
    squares.append(square) #add each of the numbers squared to the end of the list
print(squares) #print the list

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
#more efficient way to write the same code^

squares = [value**2 for value in range(1,11)]
print(squares)
#an even more efficient way to write the same code^

digits = [1,2,3,4,5,6,7,8,9,0]
min(digits) #prints smallest num in list
max(digits) #prints largest num in list
sum(digits) #prints the sum of all the num in the list
