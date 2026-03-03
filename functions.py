#decorator (hw-08)
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError, KeyError):
            return f"Enter the argument for the command"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    name = name.lower().capitalize()
    contacts[name] = phone
    return "Contact added."

@input_error
def change_phone(args, contacts):    
    name, new_phone = args

    if name in contacts:
        contacts[name] = new_phone
        return f"Contact phone number for {name} updated successfully."
    else:
        return f"Error: Contact {name} not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    name = name.lower().capitalize()

    if name in contacts:
       return f"Contact phone number for {name}: {contacts[name]}."
    else:
        return f"Error: Contact {name} not found." 

def show_all(contacts):
    result = ""
    if not contacts:
        return f"The contact dictionary is empty."
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    
    return result.strip()
