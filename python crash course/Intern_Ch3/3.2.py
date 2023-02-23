motorcyles = ['honda', 'yamaha', 'suzuki'] #created list
print(motorcyles)

motorcyles[0] = 'ducati' #changes the first item in list
print(motorcyles)

motorcyles.append('honda') #adds honda back to the end of the list
print(motorcyles)

motorcyles = [] #empties list
motorcyles.append('honda') #adds honda back to the list
motorcyles.append('yamaha') #adds yamaha back to the list behind honda
motorcyles.append('suzuki') #adds suzuki back to the list behind yamaha
print(motorcyles)

motorcyles.insert(0, 'ducati') #inserts ducati to the beginning of the list
print(motorcyles)

del motorcyles[0] #removes the first item in the list
print(motorcyles)

#Dagem
s = ["h","e","l","l","o"]
reverse = []
for letter in s:
    reverse.insert(0, letter)
print(reverse)