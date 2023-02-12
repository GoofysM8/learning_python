cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())



toppings = ['mushroom', 'onions', 'pineapple']

if 'mushroom' in toppings:
    print(True)

if 'pepperoni' not in toppings:
    print('pepperoni not avalible')



age = 12

if age < 4:
    print('Your admission cost is £0')
elif age < 18:
    print('Your admission cost is £25')
else:
    print('Your admission cost is £40')



age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f'Your admission cost is £{price}')