from collections import UserDict
from record import Record
from datetime import datetime


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, query: str):
        results = []
        query = query.lower()
        for record in self.data.values():
            attributes = [
                record.name.value.lower(),
                record.email.value.lower() if record.email else "",
                record.address.value.lower() if record.address else "",
                record.birthday.value.strftime('%d.%m.%Y') if record.birthday else "",
            ]
            attributes.extend([phone.value for phone in record.phones])     # Оскільки phones - це вже список, ми використовуємо extend
            if any(query in attr for attr in attributes):
                results.append(record)
        return results

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
            return f"Contact {name} has been deleted."
        return f"No contact with the name {name} was found."

    def get_upcoming_birthdays(self, days: int):
        upcoming_birthdays = []
        today = datetime.today().date()  
        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.date()
                birthday_this_year = birthday.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)               
                days_to_birthday = (birthday_this_year - today).days                
                if 0 <= days_to_birthday <= days:
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": birthday_this_year.strftime('%d.%m.%Y')
                    })       
        return upcoming_birthdays