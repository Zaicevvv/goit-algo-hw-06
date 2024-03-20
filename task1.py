from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record

    def find(self, name):
        if name in self.data:
            return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
	pass

class Phone(Field):
    def __init__(self, phone):
        if len(str(phone)) == 10 and all([i.isdigit() for i in str(phone)]):
            super().__init__(phone)
        else:
            raise ValueError("Phone number must be 10 digits")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old, new):
        if self.phones:
            for i, phone in enumerate(self.phones):
                if str(phone) == str(old):
                    self.phones[i] = Phone(new)
                    return
            raise ValueError("Phone number is not exist")
        else:
            raise ValueError("Phone number is not exist")

    def find_phone(self, to_find):
        if self.phones:
            for i, phone in enumerate(self.phones):
                if str(phone) == str(to_find):
                    return self.phones[i]

    def remove_phone(self, to_delete):
        if self.phones:
            for i, phone in enumerate(self.phones):
                if str(phone) == str(to_delete):
                    self.phones.pop(i)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p.value) for p in self.phones)}"

def main():
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

    # Виведення: Contact name: John, phones: 1112223333; 5555555555
    print(john)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    # Виведення: John: 5555555555
    print(f"{john.name}: {found_phone}")
    john.remove_phone("5555555555")
    print(john)

    # Видалення запису Jane
    book.delete("Jane")
    print(book.find("Jane"))

if __name__ == '__main__':
    main()