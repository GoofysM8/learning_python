cars = ['vw', 'nissan', 'mazada']
print(cars)


print(cars[0])


cars.append('honda')
print(cars)


popped_cars = cars.pop()
print(cars)
print(popped_cars)


cars.remove('nissan')
print(cars)


too_expensive = 'vw'
cars.remove(too_expensive)
print(cars)
print(f"\nA {too_expensive.title()} is too expensive.")

