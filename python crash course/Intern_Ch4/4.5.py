my_foods = ['pizza', 'falafel', 'carrot cake'] #create list
friend_foods = my_foods[:] #creates a new list with a slice of my_foods that copies the entire list
print('My favorite foods are:')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

friend_foods = my_foods[:]
my_foods.append('cannoli') #adds cannoli to the end of my list
friend_foods.append('ice cream') #adds ice cream to the end of friend's list
print('\nMy favorite foods are:')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
