with open('pi_digits.txt') as file_object:
    content = file_object.read()
print(content)


filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)


with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


filename = 'test.txt'

with open(filename, 'w') as file_object:
    file_object.write("testing")