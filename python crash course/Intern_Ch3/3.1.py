bicycles = ['trek', 'cannondale', 'redline', 'specialized'] #create list
print(bicycles)
print(bicycles[0]) #prints the first item on list without square brackets or quotations
print(bicycles[0].title()) #prints the first item in the list in title format
print(bicycles[1]) #prints the second item in the list
print(bicycles[3]) #prints the fourth item in the list

print(bicycles[-1]) #always prints the last item in the list
print(bicycles[-2]) #always prints the second to last item in the list
print(bicycles[-3]) #always prints the third to last item in the list

message = 'My first bicycle was a ' + bicycles[0].title() + '.' #creates statement, pulls the first item from the list, puts it in title format, then stores it in a variable
print(message)