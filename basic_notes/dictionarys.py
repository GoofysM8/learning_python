alien_0 = {'colour': 'green', 'points': '5'}

print(alien_0['colour'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print(f'The alien is now {alien_0["colour"]}')
alien_0['colour'] = 'red' 
print(f'The alien is now {alien_0["colour"]}')

del alien_0['points']
print(alien_0)

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

user_0 = {
    'username': 'jbob',
    'first': 'jeff',
    'last': 'bob',
    }
for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

for keys in user_0.keys():
    print(f'\n{keys.title()}')