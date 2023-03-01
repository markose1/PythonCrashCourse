def greet_user(): #defines 'greet_user'
    """Display a simple greeting.""" #one way to comment in a function
    print('Hello!') #body of the function  
greet_user() #calls the function

def greet_user(username): #creates a variable within the function
    """Display a simple greeting."""
    print('Hello, ' + username.title() + '!')
greet_user('jesse') #assigns jesse to 'username'

def describe_pet(animal_type, pet_name): 
    """Display information about a pet."""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet('hamster', 'harry') #assigns hamster and harry to the variables 
describe_pet('dog', 'willie') #assigns dog and willie to the variables and runs the function again

def describe_pet(animal_type, pet_name): 
    """Display information about a pet."""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(pet_name='harry', animal_type='hamster') #explicitly assigns hamster and harry to their intended variables 

def describe_pet(animal_type='dog', pet_name): 
    """Display information about a pet."""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(pet_name='willie') #assigns willie to 'pet_name'
describe_pet('willie') #this can also call the function
describe_pet(pet_name='harry', animal_type='hamster') #changes the variables then calls the function