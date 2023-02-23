dimensions = (200, 50) #create tuple
print(dimensions[0]) #prints first item in the tuple
print(dimensions[1]) #prints second item in the tuple
#(dimensions[0] = 250) #tries to change the value of first item in the tuple, which is not allowed

for dimension in dimensions: #loops the tuple to print both values
    print(dimension)

print('Original dimensions:')
for dimension in dimensions:
    print(dimension)
dimensions = (400,100) #modifies the values in the tuple
print('\nModified dimensions:')
for dimension in dimensions: 
    print(dimension)