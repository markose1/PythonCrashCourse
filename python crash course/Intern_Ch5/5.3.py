requested_toppings = ['mushrooms','onions','pineapple']
'mushrooms' in requested_toppings #checks if mushrooms are in the list
'pepperoni' in requested_toppings #checks if pepperonis are in the list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie' #assigns marie to user
if user not in banned_users: #checks to see if 'user' is not in 'banned_users' list
    print(user.title() + ', you can post a response if you wish.')

car = 'subaru'
print("Is car == 'subaru'? I predict true.")
car == 'subaru'
print("\nIs car == 'Audi'? I predict False.")
car == 'audi'