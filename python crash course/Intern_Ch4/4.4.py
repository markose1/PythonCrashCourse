players = ['charles', 'martina', 'michael', 'florence', 'eli'] #create list
print(players[0:3]) #prints the first 3 items in the list
print(players[1:4]) #prints the 2nd-4th items in the list
print(players[:4]) #prints the first 4 items in the list
print(players[2:]) #prints the last 3 items in the list
print(players[-3:]) #this also prints the last 3 items in the list
print('Here are the first three players on my team:')
for player in players[:3]: #prints the first 3 items from list
    print(player.title())
