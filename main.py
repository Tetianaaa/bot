import functions as func
import address_book

def main():
    try:
        book = address_book.AddressBook()
        print("Welcome to the assistant bot!")

        commands = {
            "add": func.add_contact,
            "change": func.change_phone,
            "phone": func.show_phone,
            "all": lambda args, book: func.show_all(book),
            "add-birthday" : func.add_birthday,
            "show-birthday" : func.show_birthday,
            "birthdays" : lambda args, book: func.birthdays(book),
        }

        while True:
            user_input = input("Enter a command: ")
            command, *args = func.parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command in commands:
                function = commands[command]
                print(function(args, book))
                
            else:
                print("Invalid command.")

    except ValueError as e:
        print(f'Error: {e}')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
