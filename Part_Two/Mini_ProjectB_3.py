command = ''
started = False
stopped = False

print("Welcome to the car control system!")
print("Type 'help' for a list of commands.")
while command != 'quit':
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started.')
        else:
            started = True
            print('Car started...')
    elif command == 'stop':
        if stopped:
            print('Car is already stopped.')
        else:
            stopped = True
            print('Car stopped.')
    elif command == 'help':
        print("Type 'start' to start the car.\nType 'stop' to stop the car.\nType 'quit' to exit.")
    elif command == 'quit':
        print('Exiting...')
    else:
        print("I don't understand that...")

