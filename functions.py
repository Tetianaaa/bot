import address_book

#decorator
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Please, enter name and phone."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: address_book):
    name, phone = args
    name = name.lower().capitalize()
    record = book.find(name)

    if record is None:
        record = address_book.Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_phone(args, book: address_book):    
    name, phone_number, new_number = args
    name = name.lower().capitalize()
    record = book.find(name)

    if record:
        record.edit_phone(phone_number, new_number)
        return f"Contact phone number for {name} updated successfully (from {phone_number} to {new_number})."
    else:
        return f"Error: Contact {name} not found."

@input_error
def show_phone(args, book: address_book):
    name = args[0]
    name = name.lower().capitalize()
    record = book.find(name)

    if record:
       phones = "; ".join(p.value for p in record.phones) # у випадку НЕ одного номеру
       return f"Contact {name} phone(-s): {phones}."
    else:
        return f"Error: Contact {name} not found." 

@input_error
def show_all(book: address_book):
    if not book.data:
        return f"The address book is empty."
    result = "\n".join(str(record) for record in book.data.values())
    return result


@input_error
def add_birthday(args, book: address_book):
    name, birthday = args
    name = name.lower().capitalize()
    record = book.find(name)

    if record:
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        return f"Error: Contact {name} not found."


@input_error
def show_birthday(args, book: address_book):
    name = args[0]
    name = name.lower().capitalize()
    record = book.find(name)

    if record and record.birthday:
        return f"{name}'s birthday is {record.birthday}"
    elif record and not record.birthday:
        return f"{name} do not have record about birthday."
    else:
        return f"Error: Contact {name} not found."


@input_error
def birthdays(book: address_book):
    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        return "Any upcoming birthdays in the next 7 days."
    
    birthday_list = [f"{e['name']}: {e['congratulation_date']}" for e in upcoming]

    return ", ".join(birthday_list)
