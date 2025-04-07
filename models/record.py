from .fields import Name, Phone, Email, Address, Birthday

class Record:
    """
    - ім’я (Name)
    - список телефонів (Phone)
    - email (Email)
    - адреса (Address)
    - день народження (Birthday)
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.address = None
        self.birthday = None
