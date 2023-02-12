#Make a empty list for storing aliens
aliens = []

#Make 30 aliens
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Change first aliens to the next level
for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed'] = 'faast'
        alien['points'] = 15

#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

#Show how many aliens have been created
print(f'Total number of aliens: {len(aliens)}')