#Dagem
s = ["h","e","l","l","o"]
for i in range(5):
    print(s[i]) #prints each of the items one by one
for i in range(0,5,1):
    print(s[i]) #prints each of the items one by one
for i in range(4,-1,-1):
    print(s[i]) #prints each of the items one by one
s = ["h","e","l","l","o"]
for i in range(len(s)-1,-1,-1):
    print(s[i])

reverse = []
for i in range(len(s)-1,-1,-1): #starting at end? -1 the length of list because it is inclusive
    reverse.append(s[i])
print(reverse)