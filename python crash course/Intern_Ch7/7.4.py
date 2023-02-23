prompt = '\nPlease enter the name of a city you have visited: '
prompt += "\n(Enter 'quit' when you are finished.)"
while True: #while loop will run until it reaches a 'break'
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("i'd love to go to " + city.title() + '!')

current_number = 0
while current_number < 10: 
    current_number += 1
    if current_number % 2 == 0: #if the number is even
        continue #tells python to stop the loop and go back to the beginning
    print (current_number) #prints the numbers that are not even

x = 1
while x<= 5:
    print(x)
    x += 1
#x = 1
# while x<= 5:
    #print(x)
#this will run forvever^