class Field:
    """Базовий клас для полів запису."""
    def __init__(self, value):
        self.value = value

class Name(Field):
    """Клас для зберігання імені контакту. Обов'язкове поле."""
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    """Клас для зберігання номера телефону. Має валідацію формату (10 цифр)."""
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid phone number. Must be 10 digits.")
        super().__init__(value)

    @staticmethod
    def validate(value):
        return value.isdigit() and len(value) == 10

class Record:
    """Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів."""
    def __init__(self, name, phones=None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones] if phones else []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

class AddressBook:
    """Клас для зберігання та управління записами."""
    def __init__(self):
        self.records = {}

    def add_record(self, record):
        self.records[record.name.value] = record

    def remove_record(self, name):
        if name in self.records:
            del self.records[name]

    def find_record(self, name):
        return self.records.get(name)

    def list_records(self):
        return [record for record in self.records.values()]

# Приклад використання
if __name__ == "__main__":
    book = AddressBook()
    record1 = Record(name="John Doe", phones=["1234567890"])
    book.add_record(record1)

    record2 = Record(name="Jane Smith", phones=["0987654321"])
    book.add_record(record2)

    # Додавання нового номера телефону до запису
    record1.add_phone("5556667777")

    # Видалення номера телефону з запису
    record1.remove_phone("1234567890")

    # Редагування номера телефону
    record1.edit_phone("5556667777", "1112223333")

    # Пошук запису
    record = book.find_record("Jane Smith")
    if record:
        print(f"Found: {record.name.value}, Phones: {[phone.value for phone in record.phones]}")

    # Перегляд всіх записів
    all_records = book.list_records()
    for rec in all_records:
        print(f"Name: {rec.name.value}, Phones: {[phone.value for phone in rec.phones]}")
