from .fields import Name, Phone, Email, Address, Birthday


""" 
6) Клас Record для зберігання інформації про контакт (ім'я + телефони + email + день народження)
    - ім’я (Name)
    - список телефонів (Phone)
    - день народження (Birthday)
    - email (Email)
    - адреса (Address)
    """
###
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None  # Поле день народження може бути порожнім
        self.email = None  # Поле email може бути 
        self.address = None

    '''методи для Телефонів: додавання, видалення, редагування, пошук телефону '''
    ## 6.1.1 Додавання телефону до контакту
    def add_phone(self, phone):
        self.phones.append(Phone(phone))  # Додаємо телефон у вигляді об'єкта Phone

    # 6.1.2 Видалення телефону з контакту
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    # 6.1.3 Редагування телефону в контакті
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return True
        return False

    # 6.1.4 Пошук телефону в контакті
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None


    '''методи для Дня народження додавання, видалення, редагування, пошук дня народження'''
    ## 6.2.1 Додавання дня народження до контакту
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    # 6.2.2 Видалення дня народження з контакту
    def remove_birthday(self, birthday):
        if self.birthday.value == birthday:
            self.birthday.value = None

    # 6.2.3 Редагування дня народження в контакті
    def edit_birthday(self, old_birthday, new_birthday):
        if self.birthday.value == old_birthday:
            self.birthday.value = new_birthday

    # 6.2.4 Пошук дня народження в контакті
    def find_birthday(self, birthday):
        if self.birthday.value == birthday:
                return self.birthday.value
        return None


    '''методи для Електронної пошти: додавання, видалення, редагування, пошук електронної пошти'''
    ## 6.3.1 Додавання електронної пошти до контакту
    def add_email(self, email):
        self.email = Email(email)  # Додаємо email у вигляді об'єкта Email
    
    # 6.3.2 Видалення електронної пошти з контакту
    def remove_email(self, email):
        if self.email.value == email:
            self.email.value = None
            
    # 6.3.3 Редагування електронної пошти в контакті
    def edit_email(self, old_email, new_email):
        if self.email.value == old_email:
            self.email.value = new_email
            return True
        return False
        
    # 6.3.4 Пошук електронної пошти в контакті
    def find_email(self, email):
        if self.email.value == email:
                return self.email.value
        return None
    

    '''методи для Адреси: додавання, видалення, редагування, пошук електронної пошти '''
    # 6.4.1 Додавання адреси до контакту
    def add_address(self, address):
        self.address = Address(address)  # Додаємо email у вигляді об'єкта Email
    
    # 6.4.2 Видалення адреси з контакту
    def remove_address(self, address):
        if self.address.value == address:
            self.address.value = None
            
    # 6.4.3 Редагування адреси в контакті
    def edit_address(self, new_address: str):
        if self.address:
            self.address.value = new_address
        else:
            from .fields import Address
            self.address = Address(new_address)
        
    # 6.4.4 Пошук дня адреси в контакті
    def find_address(self, address):
        if self.address.value == address:
                return self.address.value
        return None
      
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday if self.birthday else 'Not set'}, email: {self.email if self.email else 'Not set'}, address: {self.address if self.address else 'Not set'}"
