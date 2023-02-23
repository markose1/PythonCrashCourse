cars = ['bmw', 'audi', 'toyota', 'subaru'] #create list
cars.sort() #permanently puts the list in alphbetical order
print(cars)

cars.sort(reverse=True) #permanently puts list in reverse alphabetical order
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru'] #the list in original order
print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars)) #temporarily puts the list in alphabetical order until printed again

print('\nHere is the original list again:')
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru'] #the list in original order
print(cars)
cars.reverse() #reverses the order of the list permanently, but can reverse the list back to original with same function
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru'] #the list in original order
len(cars) #prints the length of the list