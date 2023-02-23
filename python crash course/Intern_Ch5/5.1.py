cars = ['audi', 'bmw', 'subaru', 'toyota'] #create list
for car in cars: #loops to grab each value from the list
    if car == 'bmw': #checks if the current value of car is bmw
        print(car.upper()) #prints bmw in all uppercase
    else:
        print(car.title()) #prints the rest of the values in title format

car = 'bmw' #assigns bmw to the variable 'car'
car == 'bmw' #checks if 'car' is equal to bmw, which is true

car = 'Audi' #assigns Audi to the variable 'car'
car == 'audi' #checks if 'car' is equal to audi, which is false due to the capitalization

car = 'Audi' #assigns Audi to the variable 'car'
car.lower() == 'audi' #it now checks if 'car' is equal to audi because it has the lowercase function, which makes it true
print(car) #but as you can see it is still saved as 'Audi'

requested_topping = 'mushrooms' #assigns mushrooms to 'requested_topping'
if requested_topping != 'anchovies': #if 'requested_topping' is not equal to anchovies
    print('Hold the anchovies!') #it will print 'Hold the anchovies!'
