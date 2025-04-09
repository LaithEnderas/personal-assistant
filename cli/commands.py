from cli.decorators import input_error
from models.address_book import AddressBook
from models.fields import Phone, Name
from models.note import Notebook, Note
from models.record import Record
"""
Функції, які відповідають за виконання команд:
- add, change, show, delete
- note-add, note-delete
- birthdays
"""
# Додає новий контакт або телефон до існуючого
@input_error
def add_contact(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        return "Enter name and phone: add_contact Name 0123456789"

    name, phone = args[0], args[1]
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        record = Record(Name(name))
        book.add_record(record)
        message = "Contact added."
    else:
        message = "New number added to existing contact."

    record.add_phone(phone)
    return message

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    if len(args) < 3:
        return "Enter name, old phone, and new phone: change_contact Name 0987654321 0501234567"

    name, old_phone, new_phone = args[0], args[1], args[2]
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        return f"Contact with name '{name}' not found."

    updated = record.edit_phone(old_phone, new_phone)
    return "Phone number updated." if updated else "Old number not found."

@input_error
def search_contacts(args: list, book: AddressBook) -> str:
    if not args:
        return "Enter a search keyword: search John"

    keyword = " ".join(args)
    found_records = book.find(keyword)

    if not found_records:
        return f"No contacts found matching: '{keyword}'"

    lines = [f"Contacts matching '{keyword}':", "-" * 30]
    for record in found_records:
        lines.append(f"Name: {record.name.value}")
        phones = ", ".join(p.value for p in record.phones)
        lines.append(f"Phones: {phones if phones else 'None'}")
        lines.append(f"Birthday: {record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'Not set'}")
        lines.append(f"Email: {record.email.value if record.email else 'Not set'}")
        lines.append(f"Address: {record.address.value if record.address else 'Not set'}")
        lines.append("")

    return "\n".join(lines).strip()

@input_error
def show_all_contacts(book: AddressBook) -> str:
    if not book.data:
        return "No contacts available."

    lines = ["Contacts:", "-" * 30]
    for record in book.data.values():
        lines.append(f"Name: {record.name.value}")

        phones = ", ".join(p.value for p in record.phones)
        lines.append(f"Phones: {phones if phones else 'None'}")

        lines.append(f"Birthday: {record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'Birthday: Not set'}")
        lines.append(f"Email: {record.email.value if record.email else 'Email: Not set'}")
        lines.append(f"Address: {record.address.value if record.address else 'Address: Not set'}")
        lines.append("")

    return "\n".join(lines).strip()

@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        return "Enter name and birthday (DD.MM.YYYY): add_birthday Name 01.01.2000"

    name, birthday_str = args[0], args[1]
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        return f"Contact with name '{name}' not found."

    try:
        record.add_birthday(birthday_str)
        return f"Birthday for {name} added: {birthday_str}"
    except ValueError as e:
        return str(e)

@input_error
def show_birthday(args: list, book: AddressBook) -> str:
    if not args:
        return "Enter contact name: show_birthday Name"

    name = args[0]
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        return f"Contact with name '{name}' not found."

    if not record.birthday:
        return f"{name} has no birthday set."

    return f"{name}'s birthday is {record.birthday.value.strftime('%d.%m.%Y') }"

@input_error
def birthdays(args: list, book: AddressBook) -> str:
    days = 7
    if args:
        try:
            days = int(args[0])
        except ValueError:
            return "Please enter a number: birthdays 10"

    result = book.get_upcoming_birthdays(days)

    if not result:
        return f"No upcoming birthdays in the next {days} days."

    lines = [f"Birthdays in the next {days} days:"]
    for entry in result:
        lines.append(f"{entry['congratulation_date']}: {entry['name']}")

    return "\n".join(lines).strip()

@input_error
def delete_contact(args: list, book: AddressBook) -> str:
    if not args:
        return "Enter the name of the contact to delete: delete_contact Name"

    name = args[0]
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        return f"Contact with name '{name}' not found."

    book.delete(name)
    return f"Contact '{name}' has been deleted."

# Додає нову нотатку до блокнота
@input_error
def add_note(args: list, notebook: Notebook):
    if not args:
        return "Enter a note: note_add Title text here"

    title = args[0]
    text = " ".join(args[1:]) if len(args) > 1 else ""
    note = Note(title=title, text=text)
    return notebook.add_note(note)

# Показує всі нотатки
@input_error
def show_notes(args: list, notebook: Notebook):
    if not notebook.notes:
        return "No notes available."

    lines = ["Notes:", "-" * 30]
    for idx, note in enumerate(notebook.notes, start=1):
        lines.append(f"{idx}. {note.text}")
    return "\n".join(lines).strip()

# Видаляє нотатку за номером
@input_error
def delete_note(args: list, notebook: Notebook):
    if not args:
        return "Enter the note title to delete: note_delete Title"

    title = args[0]

    if notebook.delete_note(title):
        return f"Note '{title}' was deleted."
    return f"Note '{title}' not found."

# Змінює текст нотатки за номером
@input_error
def edit_note(args: list, notebook: Notebook):
    if len(args) < 2:
        return "Enter note title and new text: note_edit Title Updated text"

    title = args[0]
    new_text = " ".join(args[1:])

    if notebook.edit_note(title, new_text):
        return f"Note '{title}' updated."
    return f"Note '{title}' not found."

# Шукає нотатки, що містять ключове слово
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
