import pickle
from address_book import AddressBook

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    # не лише у випадку відсутності файлу
    # також якщо попередньо нічого не було записано у файл і він порожній/пошкодженний
    except (FileNotFoundError, EOFError, pickle.UnpicklingError):
        return AddressBook()
