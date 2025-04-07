class Field:
    """Базовий клас для полів контакту."""
    def __init__(self, value):
        self.value = value


class Name(Field):
    """Поле для імені контакту."""
    pass


class Phone(Field):
    """Поле для номера телефону. Має перевіряти, що це 10 цифр."""
    pass


class Email(Field):
    """Поле для email. Має перевіряти коректність формату."""
    pass


class Address(Field):
    """Поле для адреси."""
    pass


class Birthday(Field):
    """Поле для дня народження у форматі DD.MM.YYYY."""
    pass
