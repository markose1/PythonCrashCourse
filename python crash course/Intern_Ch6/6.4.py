pizza = { #create dictionary
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'] #assigning multiple values to one key
}
print('You ordered a ' + pizza['crust'] + '-crust pizza' + 'with the following toppings:')
for toppings in pizza['toppings']: #grabs all of the values from the key
    print('\t' + toppings) #prints those values

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil': ['python','haskell'], 
}
for name, languages in favorite_languages.items(): #grabs both the keys and their values
    print('\n' + name.title() + "'s favorite languages are:") #prints a name first
    for language in languages:
        print('\t' + language.title()) #then the values assigned to that key

users = {
    'aeinstein':{
    'first':'albert',
    'last':'einstein',
    'location':'princeton'
    }, #creates a dictionary within a dictionaery
    'mcurie':{
    'first':'marie',
    'last':'curie',
    'location':'paris'
    },
}
for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('\tFull name: ' + full_name.title())
    print('\tLocation ' + location.title())