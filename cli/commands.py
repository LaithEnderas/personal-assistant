from cli.decorators import input_error
from models.address_book import AddressBook, Record, Phone, Name
from models.note import Notebook, Note
"""
Функції, які відповідають за виконання команд:
- add, change, show, delete
- note-add, note-delete
- birthdays
"""
@input_error
def add_contact(args: list, book: AddressBook):
    if len(args) < 2:
        return "Enter name and phone: add_contact Name 0123456789"
    
    name, phone = args[0], args[1]
    record = book.find(name)
    
    if not record:
        record = Record(Name(name))
        book.add_record(record)
        message = "Contact added."
    else:
        message = "New number added to existing contact."
    
    record.add_phone(phone)
    return message

@input_error
def change_contact(args: list, book: AddressBook):
    if len(args) < 3:
        return "Enter name, old phone, and new phone: change_contact Name 0987654321 0501234567"
    
    name, old_phone, new_phone = args[0], args[1], args[2]
    record = book.find(name)
    
    if not record:
        return f"Contact with name '{name}' not found."
    
    updated = record.edit_phone(old_phone, new_phone)
    if updated:
        return "Phone number updated."
    else:
        return "Old number not found."

@input_error
def phone_username(args: list, book: AddressBook):
    if not args:
        return "Enter contact name: phone Name"
    
    name = args[0]
    record = book.find(name)
    
    if not record:
        return f"Contact with name '{name}' not found."
    
    phones = ", ".join(p.value for p in record.phones)
    return  f"{name}'s phone numbers: {phones}" if phones else f"Contact '{name}' has no phone numbers."

@input_error
def show_all_contacts(book: AddressBook):


    if not book.data:
        return "No contacts available."
    
    lines = ["Contacts:", "-" * 30] # виведення заголовка Contacts
    for record in book.data.values():
        lines.append(f"Name: {record.name.value}")
        
        phones = ", ".join(p.value for p in record.phones)
        lines.append(f"Phones: {phones if phones else 'None'}")
        
        if record.birthday:
            lines.append(f"Birthday: {record.birthday.value.strftime('%d.%m.%Y')}")
        else:
            lines.append("Birthday: Not set") # Якщо поле відсутнє 

        if record.email:
            lines.append(f"Email: {record.email.value}")
        else:
            lines.append("Email: Not set")

        if record.address:
            lines.append(f"Address: {record.address.value}")
        else:
            lines.append("Address: Not set")

        lines.append("")

    return "\n".join(lines).strip()

@input_error
def delete_contact(args: list, book: AddressBook):
    if not args:
        return "Enter the name of the contact to delete: delete_contact Name"
    
    name = args[0]
    record = book.find(name)
    
    if not record:
        return f"Contact with name '{name}' not found."
    
    book.delete(name)
    return f"Contact '{name}' has been deleted."

@input_error
def add_birthday(args: list, book: AddressBook):
    if len(args) < 2:
        return "Enter name and birthday (DD.MM.YYYY): add_birthday Name 01.01.2000"

    name, birthday_str = args[0], args[1]
    record = book.find(name)

    if not record:
        return f"Contact with name '{name}' not found."

    try:
        record.add_birthday(birthday_str)
        return f"Birthday for {name} added: {birthday_str}"
    except ValueError as e:
        return str(e)
    
@input_error
def show_birthday(args: list, book: AddressBook):
    if not args:
        return "Enter contact name: show_birthday Name"

    name = args[0]
    record = book.find(name)

    if not record:
        return f"Contact with name '{name}' not found."

    if not record.birthday:
        return f"{name} has no birthday set."

    return f"{name}'s birthday is {record.birthday.value.strftime('%d.%m.%Y')}"

@input_error
def birthdays(args: list, book: AddressBook):
    day = 7 # дефолтне значення при введені команди без агрументів
    
    if args:
        try:
            days = int(args[0])
        except ValueError:
            return "Please enter a number: birthdays 10"
    result = book.get_upcoming_birthdays(days)
    
    if not any(result.values()):
        return f"No upcoming birthdays in the next {days} days."
    
    lines = [f"Birthdays in the next {days} days:"]
    for day, names in result.items():
        if names:
            lines.append(f"{day}: {', '.join(names)}")
    
    return "\n".join(lines).strip()

@input_error
def add_note(args: list, notebook: Notebook):
    if not args:
        return "Enter a note: note_add text here"
    text = " ".join(args)
    note = Note(text)
    notebook.add_note(note)
    return "Note added"

@input_error
def show_notes(args: list, notebook: Notebook):
    if not notebook.notes:
        return "No notes available."
    
    lines = ["Notes:", "-" * 30]
    for idx, note in enumerate(notebook.notes, start=1):
        lines.append(f"{idx}. {note.text}")
    return "\n".join(lines).strip()

@input_error
def delete_note(args: list, notebook: Notebook):
    if not args:
        return "Enter note number to delete: note_delete 1"
    try:
        note_index = int(args[0]) - 1
        deleted_note = notebook.delete_note(note_index)
        return f"Note deleted: {deleted_note.text}"
    except (IndexError, ValueError):
        return "Invalid note number."

@input_error
def edit_note(args: list, notebook: Notebook):
    if len(args) <2:
        return "Enter note number and new text: note_edit 1 Updated text here"
    
    try:
        note_index = int(args[0]) - 1
        new_text = " ".join(args[1:])
        edited_note = notebook.edit_note(note_index, new_text)
        return f"Note updated: {edited_note.text}"
    except (IndexError, ValueError):
        return "Invalid note number."
    
@input_error
def search_notes(args: list, notebook: Notebook):
    if not args:
        return "Enter keyword to search notes: note_search keyword"
    
    keyword = " ".join(args).lower()
    results = notebook.search_notes(keyword)
    
    if not results:
        return f"No notes found for keyword: '{keyword}'"
    
    lines = [f"Notes matching '{keyword}':", "-" * 30]
    for idx, note in enumerate(results, start=1):
        lines.append(f"{idx}. {note.text}")
    return "\n".join(lines).strip()

        
           
    
        