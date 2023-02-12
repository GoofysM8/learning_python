current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = '\nWrite something: '
prompt += "\nEnter 'quit' to end the program. "
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)


active = True
while active:
    message = input("type 'done' to quit: ")

    if message == 'done':
        active = False
    else:
        print(message)