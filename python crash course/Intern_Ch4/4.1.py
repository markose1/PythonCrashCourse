magicians = ['alice', 'david', 'carolina'] #create list
for magician in magicians: #create a 'for' loop, which takes a name from list and stores it in variable until they are all stored
    print(magician) #prints the variable that contains each item in the list

for magician in magicians:
    print(magician.title() + ', that was a great trick!') #takes each name from list, puts them in title format then inserts them into statement
    print("I can't wait to see your next trick, " + magician.title() + '.\n') #the \n in the print statement inserts a blank line after each pass thru the loop

print('Thank you, everyone. That was a great magic show!') #not in the loop so it is only printed once
