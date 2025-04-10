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

# ==================== ФУНКЦІЇ ДЛЯ РОБОТИ З ТЕЛЕФОНАМИ ===================================

# Додає новий контакт або телефон до існуючого
@input_error
def add_contact(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        return "Enter name and phone: add_contact Name 0123456789"

    name, phone = args[0].capitalize(), args[1]
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

# Змінює старий контакт на новий
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


# Пошук контактів по будь-якому критерію, видає всі збіги
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


# Виводить усі контакти
@input_error
def show_all_contacts(book: AddressBook) -> str:
    if not book.data:
        return "No contacts available."

    lines = ["Contacts:", "-" * 100]
    header = f"{'Name':<20} {'Phones':<25} {'Birthday':<15} {'Email':<25} {'Address'}"
    lines.append(header)
    lines.append("-" * 100)

    for record in book.data.values():
        name = str(record.name.value)
        phones = ", ".join(p.value for p in record.phones) or "None"
        birthday = record.birthday.value.strftime('%d.%m.%Y') if record.birthday else "Not set"
        email = record.email.value if record.email else "Not set"
        address = record.address.value if record.address else "Not set"
        lines.append(f"{name:<20} {phones:<25} {birthday:<15} {email:<25} {address}")

    return "\n".join(lines).strip()

# Видаляє контакт
@input_error
def delete_contact(args: list, book: AddressBook) -> str:
    if not args:
        return "Enter the name of the contact to delete: delete_contact Name"

    name = args[0]
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        return f"Contact with name '{name}' not found."

    book.delete(record.name.value)
    return f"Contact '{name}' has been deleted."



# ==================== ФУНКЦІЇ ДЛЯ РОБОТИ З ДАТОЮ ДНЯ НАРОДЖЕННЯ ===================================

# Додає день народження
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

# Виводить день народження контакту за іменем
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


# Виводить список контактів в яких день народження за n-днів
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

    lines = [f"Birthdays in the next {days} days:", "-" * 40]
    for entry in result:
        lines.append(f"{entry['congratulation_date']:<15} {entry['name']}")

    return "\n".join(lines).strip()




# ==================== ФУНКЦІЇ ДЛЯ РОБОТИ З НОТАТКАМИ ===================================


# Додає нову нотатку до блокнота
@input_error
def add_note(args: list, notebook: Notebook) -> str:
    if not args:
        return "Enter a note: add-note Title text here"

    title = args[0]
    text = " ".join(args[1:]) if len(args) > 1 else ""
    note = Note(title=title, text=text)
    added_note = notebook.add_note(note)

    if added_note:
        return f"Note '{title}' was added."
    else:
        return f"Note with title '{title}' already exists."

# Показує всі нотатки
@input_error
def show_notes(args: list, notebook: Notebook) -> str:
    if not notebook.notes:
        return "No notes available."

    lines = ["Notes:", "-" * 80]
    header = f"{'Title':<20} {'Text':<40} {'Tags':<20}"
    lines.append(header)
    lines.append("-" * 80)

    for note in notebook.notes:
        title = note.title
        text = (note.text[:37] + '...') if len(note.text) > 40 else note.text
        tags = ", ".join(note.tags) if note.tags else ""
        lines.append(f"{title:<20} {text:<40} {tags:<20}")

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


# ==================== ФУНКЦІЇ ДЛЯ РОБОТИ З EMAIL ===================================

# Додає ел. пошту
@input_error
def add_email(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        return "Enter name and email: add_email Name email@example.com"

    name, email = args[0], args[1]
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        return f"Contact with name '{name}' not found."

    record.add_email(email)
    return f"Email for {name} added: {email}"

# Змінює ел. пошту
@input_error
def change_email(args: list, book: AddressBook) -> str:
    if len(args) < 3:
        return "Enter name, old email, and new email: edit_email Name old@example.com new@example.com"

    name, old_email, new_email = args[0], args[1], args[2]
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record or not record.email:
        return f"Contact with name '{name}' not found or email not set."

    record.edit_email(old_email, new_email)
    return f"Email for {name} updated to: {new_email}"


# ==================== ФУНКЦІЇ ДЛЯ РОБОТИ З АДРЕСОЮ ===================================

# Додає адресу
@input_error
def add_address(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        return "Enter name and address: add_address Name Some Street 123"

    name, address = args[0], " ".join(args[1:])
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        return f"Contact with name '{name}' not found."

    record.add_address(address)
    return f"Address for {name} added: {address}"

# Змінює адресу
@input_error
def edit_address(args: list, book: AddressBook) -> str:
    if len(args) < 3:
        return "Enter name, old address, and new address: edit_address Name Old St 1 New St 2"

    name, old_address = args[0], args[1]
    new_address = " ".join(args[2:])
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record or not record.address:
        return f"Contact with name '{name}' not found or address not set."

    record.edit_address(old_address, new_address)
    return f"Address for {name} updated to: {new_address}"


# ==================== ФУНКЦІЇ ДЛЯ РОБОТИ З ТЕГАМИ ===================================

# Додає тег до нотатки за назвою
@input_error
def add_tag(args: list, notebook: Notebook) -> str:
    if len(args) < 2:
        return "Enter note title and tag: add_tag Title Tag"

    title, tag = args[0], args[1]
    for note in notebook.notes:
        if note.title == title:
            note.add_tag(tag)
            return f"Tag '{tag}' added to note '{title}'."
    return f"Note with title '{title}' not found."

# Cортує всі нотатки за тегами та виводить їх у зручному вигляді.
@input_error
def sort_notes_by_tag(args: list, notebook: Notebook) -> str:
    if not notebook.notes:
        return "No notes available."

    sorted_notes = notebook.sort_notes_by_tag()
    lines = ["Sorted Notes by Tag:", "-" * 70]
    header = f"{'#':<3} {'Title':<20} {'Tags':<20} {'Text'}"
    lines.append(header)
    lines.append("-" * 70)
    for idx, note in enumerate(sorted_notes, start=1):
        tags = ", ".join(note.tags) if note.tags else "no tags"
        lines.append(f"{idx:<3} {note.title:<20} {tags:<20} {note.text}")

    return "\n".join(lines).strip()