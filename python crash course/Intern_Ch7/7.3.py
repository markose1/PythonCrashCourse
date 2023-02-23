current_number = 1 #assigns 1 to 'current_number'
while current_number <= 5: #while 'current_number' is <= 5
    print(current_number) #print 'current_number'
    current_number += 1 #add 1 to 'current_number'

prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program. "
message = ''
while message != 'quit': #while 'message' does not = quit
    message = input(prompt) #assign the input to 'message', which comes after the prompt
    print(message)

prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program. "
active = True #sets 'active' to True
while active: #while 'active' is true
    message = input(prompt) #assign the input to 'message', which comes after the prompt
    if message == 'quit': #if message is equal to quit
        active = False #sets 'active' to false
    else:
        print(message)