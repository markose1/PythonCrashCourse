alien_o = {'color': 'green', 'points': 5} #create dictionary
print(alien_o['color']) #print 'color' value from dictionary
print(alien_o['points']) #print 'points' value from dictionary

new_points = alien_o['points'] #grabs the value of 'points' from dictionary
print('you just earned ' + str(new_points) + ' points!')

alien_o = {}
alien_o['color'] = 'green' #adds 'color' and its value to the dictionary
alien_o['points'] = 5 #adds 'points' and its value to the dictionary
alien_o['x_position'] = 0 #adds 'x_position' and its value to the dictionary
alien_o['y_position'] = 25 #adds 'y_position' and its value to the dictionary
print(alien_o)

print('The alien is ' + alien_o['color'] + '.')
alien_o['color'] = 'yellow' #changes 'color' value in the dictionary to yellow
print('The alien is now ' + alien_o['color'] + '.')

alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position:' + str(alien_o['x_position']))
if alien_o['speed'] == 'slow': #if the value of 'speed' is 'slow' 'x_increment' is 1
    x_increment = 1
elif alien_o['speed'] == 'medium': #if the value of 'speed' is 'medium' 'x_increment' is 2
    x_increment = 2
else: #anything else, 'x_increment' is 3
    x_increment = 3
alien_o['x_position'] = alien_o['x_position'] + x_increment #assigns the value of 'x_position' to the current value + x_increment
print('New x-position' + str(alien_o['x_position']))

alien_o = {'color': 'green', 'points': 5}
print(alien_o)
del alien_o['points'] #deletes 'points' and its value from the dictionary