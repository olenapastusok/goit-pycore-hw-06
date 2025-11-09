from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Зберігання імені контакту"""
    def __init__(self, value):
        super().__init__(value)
        if not value:
            raise ValueError("Name cannot be empty")

class Phone(Field):
    """Клас, який забезпечує валідацію номера телефону"""
    def number_validation(self, value):
        """перевірка на 10 цифр"""
        if value.isdigit() and len(value) == 10:
            return value
        else: 
             return ValueError("Phone number shoud have 10 digits")
        

class Record:
    """Клас, який відповідає за додавання, видалення, редагування та пошук телефонів"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """Додавання нового телефону"""
        return self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        """Видаляє номер телефону, який вказано на вхід"""
        for ph in self.phones:
            if ph.values == phone:
                self.phones.remove(ph)
                return True
        return False
    
    def edit_phone(self, old_phone, new_phone):
        """Змінює старий номер телефону на новий"""
        for i, ph in enumerate(self.phones):
            if ph.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False
    
    def find_phone(self, phone):
        """Пошук телефону в записах"""
        for ph in self.phones:
            if ph.value == phone:
                return ph.value
        return None
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """" Клас, який відповідає за додавання нових записів, пошук записів за іменем та видалення записів за іменем"""
    def add_record(self, record):
        """Функція додавання нових записів"""
        self.data[record.name.value] = record
    
    def find(self, name):
          """Знаходить запис за вказаним іменем"""
          return self.data.get(name)

    def delete(self, name):
        """Видалення записів за іменем"""
        if name in self.data:
            del self.data[name]
        

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону в записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
