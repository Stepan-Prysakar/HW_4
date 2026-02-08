from collections import UserDict

# Базовий клас для полів запису.
class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

# Клас для зберігання імені контакту. 
class Name(Field):
    pass

# Клас для зберігання номера телефону з валідацією.
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError('Номер повинен містити 10 цифр')
        super().__init__(value)

# Клас для зберігання інформації про контакт та методами маніпуляції з нею
class Record:
    def __init__(self, name):
        self.name = Name(name)      # ім'я екземпляру - об'єкт класу Name
        self.phones = []        # список номерів екземпляру

    def add_phone(self, phone):        
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        try:
            self.phones.remove(self.find_phone(phone))
        except:
            raise Exception(f'Контакт {self.name} не містить вказаний номер')
        
    def edit_phone(self, phone, new_phone):
        if self.find_phone(phone):
            self.add_phone(new_phone)
            self.remove_phone(phone) 
        else:
            raise ValueError('Не вірні вхідні дані')

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i

    def __str__(self):    # реалізація user-friendly виводу
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# Клас для зберігання та управління записами.
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]
     
    def __str__(self):    # реалізація user-friendly виводу      
        return "\n".join(str(r) for r in self.data.values())
               
book = AddressBook()
john_record = Record('John')
john_record.add_phone('0969182298')
john_record.add_phone('1111111111')
book.add_record(john_record)
jane_record = Record('Jane')
jane_record.add_phone('2222222222')
jane_record.add_phone('3333333333')
book.add_record(jane_record)


