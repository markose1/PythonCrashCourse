for value in range(1,21): #prints all the numbers between 1-4
    print(value)

numbers = list(range(1,1000001)) #prints all the numbers between 1-1,000,000 but in a list
min(numbers)
max(numbers)
sum(numbers)

odd_numbers = list(range(1,20,2))
print(odd_numbers)

multiples_of_three = list(range(3,31,3))
print(multiples_of_three)

cubes = [value**3 for value in range(1,11)]
print(cubes)