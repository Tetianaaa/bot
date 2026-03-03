import functions as func

def main():
    try:
        contacts = {}
        print("Welcome to the assistant bot!")
        while True:
            user_input = input("Enter a command: ")
            command, *args = func.parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(func.add_contact(args, contacts))
            elif command == 'change':
                print(func.change_phone(args, contacts))
            elif command == 'phone':
                print(func.show_phone(args, contacts))
            elif command == 'all':
                print(func.show_all(contacts))
            
            else:
                print("Invalid command.")

    except ValueError as e:
        print(f'Error: {e}')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
