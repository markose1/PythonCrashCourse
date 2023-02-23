favorite_languages = { #create dictionary
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + '.')

user_o = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_o.items(): #to create a for loop for dictionaries, you create names for the two variables that will hold the key and value
    print('\nKey:' + key)
    print('Value:' + value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items(): #grabs all of the keys and their values from the list
    print(name.title() + "'s favorite language is " + language.title() + '.')

for name in favorite_languages.keys(): #grabs all of the keys from the dictionary
    print(name.title())
#(for name in favorite_languages:) does the same loop

friends = ['sarah','phil'] #create list of names we want to print
for name in favorite_languages:
    print(name.title())
if name in friends: #grabs the names from the created list
    print('Hi ' + name.title() + ', I see your favorite language is ' + favorite_languages[name].title() + '!')

if 'erin' not in favorite_languages: #checks to see if erin is not in the dictionary
    print('Erin, please take our poll!')

for name in sorted(favorite_languages.keys()): #sorts all the keys before looping them
    print(name.title() + ', thank you for taking the poll.')

print('The following languages have been mentioned:')
for language in favorite_languages.values(): #grabs all of the values from the dictionary
    print(language.title())

print('The following languages have been mentioned:')
for language in set(favorite_languages.values()): #because it is in a set it only prints out each value once
    print(language.title())