responses = {}
polling_active = True #sets 'polling_active' to True
while polling_active: #while 'polling_active' is set to true 
    name = input('\nWhat is your name?') #assigns input to 'name'
    response = input('Which mountain would you like to climb someday?') #assigns input to 'response'
    responses[name] = response #assigns 'response' as a value to 'name' in the 'responses' dictionary
    repeat = input('Would you like to let another person respond? (yes/no)') #assigns input to 'repeat'
    if repeat == 'no': #if 'repeat' is equal to no
        polling_active = False #flags 'polling_active' to stop loop
print('\n--- Poll Results ---')
for name, response in responses.items(): 
    print(name + ' would like to climb ' + response + '.')