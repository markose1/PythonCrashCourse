unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users: #grabs each of the unconfirmed users
    current_user = unconfirmed_users.pop() #deletes the unconfirmed user from the list then assigns them to 'current_user'
    print('verifying user: ' + current_user.title())
    confirmed_users.append(current_user) #add the 'current_user' to 'confirmed_users' list
print('\nThe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets: #grabs all of the cats in the list
    pets.remove('cat') #and removes them
print(pets)
