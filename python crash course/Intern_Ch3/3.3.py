motorcyles = ['honda', 'yamaha', 'suzuki'] #create list
popped_motorcycle = motorcyles.pop() #removes the last item in the list and stores that item in a variable
print(motorcyles) #prints the updated list
print(popped_motorcycle) #prints the item in the list that was removed

motorcyles = ['honda', 'yamaha', 'suzuki'] #restore the list back to how it was
last_owned = motorcyles.pop() #removes and stores the last item from the list in a variable
print('The last motorcycle I owned was a ' + last_owned.title() + '.') #prints the popped item in a statement

motorcyles = ['honda', 'yamaha', 'suzuki'] #restore the list back to how it was
first_owned = motorcyles.pop(1) #removes and stores the second item from the list in a variable
print('The last motorcycle I owned was a ' + last_owned.title() + '.') #prints the popped item in a statement

motorcyles = ['honda', 'yamaha', 'suzuki', 'ducati'] #create list
print(motorcyles)
motorcyles.remove('ducati') #tells python to find and remove ducati from the list
print(motorcyles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] #restore list to original
print(motorcycles)
too_expensive = 'ducati' #store ducati in a variable called too expensive
motorcycles.remove(too_expensive) #uses the variable to remove item from the list
print(motorcyles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.') #created a statement explaning why ducati was removed from the list