from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        # перевірка чи це число і чи є 10 цифр
        if not value.isdigit() or len(value) != 10:
             raise ValueError("Phone number must have 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
         self.phones.append(Phone(phone_number))
    
    # перезапис списку номерів, які відмінні від того, що на видалення
    def remove_phone(self, phone_number):
         self.phones = [p for p in self.phones if p.value != phone_number]
    
    def edit_phone(self, phone_number, new_number):
        for i, phone in enumerate(self.phones):
            if phone.value == phone_number:
                self.phones[i] = Phone(new_number)
                return 
        raise ValueError(f"Phone {phone_number} not found in records.")
    
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday):
         self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    #додає запис до self.data
    def add_record(self, record):
        self.data[record.name.value] = record

    # знаходить запис за ім'ям
    def find(self, name):
        return self.data.get(name)

    # видаляє запис за ім'ям
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):

        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue
            
            birthday = record.birthday.value
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= 7:
                congratulation_date = birthday_this_year
            
                if congratulation_date.weekday() == 5:
                        congratulation_date += timedelta(days=2)
                
                elif congratulation_date.weekday() == 6:
                        congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime('%d.%m.%Y')
                    })

        return upcoming_birthdays
