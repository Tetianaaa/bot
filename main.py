import functions as func
import serialization

def main():
    try:
        book = serialization.load_data()  

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
                serialization.save_data(book)
                print("Good bye! Your data is saved")
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
