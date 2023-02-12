message = input('Write something: ')
print(message)


customers = input('How many people are coming tonight: ')
customers = int(customers)
if customers >= 8:
    print('There is a waiting time of 30 mins')
else:
    print('Your table is ready')
