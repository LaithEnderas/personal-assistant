import re
from datetime import datetime

""" 1) Базовий клас для полів контакту."""
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


""" 2) Поле для імені контакту."""
class Name(Field):
    def __init__(self, value):
        value = value.strip().capitalize()  # Капіталізація

        if not value:
            raise ValueError("Name cannot be empty")

        if not re.match(r"^[A-Za-zÀ-ÿ'\- ]+$", value):
            raise ValueError("Name must contain only letters, hyphens, apostrophes, or spaces")

        super().__init__(value)


""" 3) Поле для номера телефону. Має перевіряти, що це 10 цифр."""
class Phone(Field):
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid phone number. Must be 10 digits.")
        super().__init__(value)

    # Валідація формату телефону (10 цифр)
    @staticmethod
    def is_valid(phone):
        return bool(re.match(r"^\d{10}$", phone))


""" 4) Поле для email. Має перевіряти коректність формату."""
class Email(Field):
    def __init__(self, value):
        value = value.strip().lower()  # Привезведення до нижнього регістру

        if not self.is_valid(value):
            raise ValueError("Invalid email format.")
        super().__init__(value)

    # Валідація формату електронної пошти
    @staticmethod
    def is_valid(email):
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))              # [^@]+ : означає "одне або більше будь-яких символів, крім символу @". Це перевіряє першу частину email до знака @ (локальна частина).
                                                                         # @     : перевіряє наявність символа @.
                                                                         # [^@]+ : означає "одне або більше будь-яких символів, крім @". Це перевіряє доменну частину до крапки (наприклад, gmail).
                                                                         # \.    : екранує крапку, оскільки в регулярних виразах крапка — це спеціальний символ, що означає "будь-який символ". Тому потрібно використовувати зворотний слеш перед нею.
                                                                         # [^@]+: перевіряє частину після крапки (зазвичай це домен верхнього рівня, наприклад, com, org, net тощо).

""" 5) Поле для адреси."""
class Address(Field):
    def __init__(self, value):
        self.value = value


""" 6) Поле для дня народження у форматі DD.MM.YYYY."""
class Birthday(Field):
    def __init__(self, value):
        try:
            # Перевірка формату дати: DD.MM.YYYY
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
