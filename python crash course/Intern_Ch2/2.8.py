favorite_language = 'python '
print(favorite_language.rstrip()) #strips whitespace from the end of the statement
print(favorite_language) #the whitespace returns

favorite_language = favorite_language.rstrip() #changes statment to keep the whitespace out by storing it in a variable
print(favorite_language)

favorite_language = ' python '
print(favorite_language.lstrip()) #strips whitespace from the beginning of the statement
print(favorite_language.strip()) #strips whitespace from both ends of the statement

#Dagem
message = ' remove the white space in the front and back '
message2 = 'Put this string with the other one and make them one'
message3 = (message.strip() + ' ' + message2)
print(message3.upper())