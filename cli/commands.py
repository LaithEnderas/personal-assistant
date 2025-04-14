from cli.decorators import input_error
from models.address_book import AddressBook
from models.fields import Phone, Name
from models.note import Notebook, Note
from models.record import Record
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from cli.rich_table import print_message
from rich.text import Text
import difflib



"""
Функції, які відповідають за виконання команд:
- add, change, show, delete
- note-add, note-delete
- birthdays
"""
KNOWN_COMMANDS = [
    "add", "change", "search", "all", "add-birthday", "show-birthday", "birthdays",
    "delete", "add-note", "delete-note", "search-note", "add-email", "edit-email",
    "add-address", "edit-address", "add-tag", "search-by-tag", "sort-notes-by-tag"
]

console = Console()

@input_error
def help_command(*args):
    from cli.rich_table import show_command_table
    show_command_table()
    return "Type a command to continue"


# ==================== ФУНКЦІЇ ДЛЯ РОБОТИ З ТЕЛЕФОНАМИ ===================================

# Додає новий контакт або телефон до існуючого
@input_error
@input_error
def add_contact(args: list, book: AddressBook):
    if len(args) < 2:
        return "Enter name and phone: add Name 0123456789"

    name_str = args[0]
    phone = args[1]

    record_list = book.find(name_str)
    record = record_list[0] if record_list else None

    if not record:
        record = Record(name_str)  # здесь передаём строку, Record сам создаёт Name
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
        return"Enter name, old phone, and new phone: change_contact Name 0987654321 0501234567"

    name, old_phone, new_phone = args[0], args[1], args[2]
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        return f"Contact with name '{name}' not found."

    updated = record.edit_phone(old_phone, new_phone)
    return "Phone number updated." if updated else "Old number not found."

# Пошук контактів по будь-якому критерію, видає всі збіги
@input_error
def search_contacts(args: list, book: AddressBook):
    if not args:
        return"Enter a search keyword: search John"

    keyword = " ".join(args)
    found_records = book.find(keyword)

    if not found_records:
        return f"No contacts found matching: '{keyword}'"

    console = Console()
    table = Table(title=f"Contacts matching '{keyword}'")
    table.add_column("Name", style="cyan")
    table.add_column("Phones", style="green")
    table.add_column("Birthday", style="magenta")
    table.add_column("Email", style="yellow")
    table.add_column("Address", style="white")

    for record in found_records:
        name = str(record.name.value)
        phones = ", ".join(p.value for p in record.phones) or "None"
        birthday = record.birthday.value.strftime('%d.%m.%Y') if record.birthday else "Not set"
        email = record.email.value if record.email else "Not set"
        address = record.address.value if record.address else "Not set"
        table.add_row(name, phones, birthday, email, address)

    console.print(table)
    return ""

# Виводить усі контакти
@input_error
def show_all_contacts(book: AddressBook):
    if not book.data:
        console.print("[bold yellow]No contacts available.[bold yellow]")

    console = Console()
    table = Table(title="All Contacts")

    table.add_column("Name", style="cyan")
    table.add_column("Phones", style="green")
    table.add_column("Birthday", style="magenta")
    table.add_column("Email", style="yellow")
    table.add_column("Address", style="white")

    for record in book.data.values():
        name = str(record.name.value)
        phones = ", ".join(p.value for p in record.phones) or "None"
        birthday = record.birthday.value.strftime('%d.%m.%Y') if record.birthday else "Not set"
        email = record.email.value if record.email else "Not set"
        address = record.address.value if record.address else "Not set"
        table.add_row(name, phones, birthday, email, address)

    console.print(table)
    return ""


# Видаляє контакт
@input_error
def delete_contact(args: list, book: AddressBook):
    if not args:
        return "Enter the name of the contact to delete: delete_contact Name"

    name_input = args[0].strip().lower()

    for name_obj in book.data:
        if name_obj.value.lower() == name_input:
            book.delete(name_obj)  # передаємо Name-об’єкт
            return f"Contact '{name_obj.value}' has been deleted."

    return f"Contact with name '{args[0]}' not found."


# ==================== ФУНКЦІЇ ДЛЯ РОБОТИ З ДАТОЮ ДНЯ НАРОДЖЕННЯ ===================================

# Додає день народження
@input_error
def add_birthday(args: list, book: AddressBook):
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
def show_birthday(args: list, book: AddressBook):
    if not args:
        return "Enter contact name: show-birthday Name"
        

    name = args[0]
    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        return f"Contact with name '{name}' not found."
        

    if not record.birthday:
        return f"{name} has no birthday set."
        

    birthday_str = record.birthday.value.strftime('%d.%m.%Y')
    return f"{name}'s birthday is {birthday_str}"

# Виводить список контактів в яких день народження за n-днів
@input_error
def birthdays(args: list, book: AddressBook) -> str:
    console = Console()

    try:
        days = int(args[0]) if args else 7
    except ValueError:
        return "Please enter a number: birthdays 10"

    result = book.get_upcoming_birthdays(days)

    if not result:
        return f"No upcoming birthdays in the next {days} days."

    # Сортуємо за датою
    sorted_result = sorted(result, key=lambda entry: datetime.strptime(entry['congratulation_date'], '%d.%m.%Y'))

    # Побудова таблиці
    table = Table(title=f"🎉 Birthdays in the next {days} days", title_style="bold magenta")
    table.add_column("Date", style="cyan", justify="center")
    table.add_column("Name", style="bold green")

    for entry in sorted_result:
        table.add_row(entry["congratulation_date"], str(entry["name"]))

    console.print(table)
    return ""  # Повертаємо порожній рядок, щоб не було None



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


# Видаляє нотатку за номером
@input_error
def delete_note(args: list, notebook: Notebook):
    if not args:
        console.print("[bold yellow]Enter the note title to delete: note_delete Title[bold yellow]")

    title = args[0]

    if notebook.delete_note(title):
        return f"Note '{title}' was deleted."
    return f"Note '{title}' not found."

# Змінює текст нотатки за номером
@input_error
def edit_note(args: list, notebook: Notebook):
    if len(args) < 2:
        console.print("[bold yellow]Enter note title and new text: note_edit Title Updated text[bold yellow]")

    title = args[0]
    new_text = " ".join(args[1:])

    if notebook.edit_note(title, new_text):
        return f"Note '{title}' updated."
    return f"Note '{title}' not found."

# Шукає нотатки, що містять ключове слово
@input_error
def search_notes(args: list, notebook: Notebook):
    console = Console()

    if not args:
        console.print("[yellow]Enter keyword to search notes: note_search keyword[yellow]")

    keyword = " ".join(args).lower()
    results = notebook.search_notes(keyword)

    if not results:
        console.print( f"[red]No notes found for keyword: '{keyword}'[/red]")

    table = Table(title=f"📝 Notes matching '{keyword}'", title_style="bold cyan")
    table.add_column("№", style="dim", justify="center")
    table.add_column("Title", style="bold green")
    table.add_column("Text", style="white")
    table.add_column("Tags", style="yellow")

    for idx, note in enumerate(results, start=1):
        tags = ", ".join(note.tags) if note.tags else "no tags"
        table.add_row(str(idx), note.title, note.text, tags)

    console.print(table)
    return ""

# ==================== ФУНКЦІЇ ДЛЯ РОБОТИ З EMAIL ===================================

# Додає ел. пошту
@input_error
def add_email(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        console.print("[bold yellow]Enter name and email: add_email Name email@example.com[bold yellow]")

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
        console.print("[bold yellow]Enter name, old email, and new email: edit_email Name old@example.com new@example.com[bold yellow]")

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
def edit_address(args: list, book):
    console = Console()

    if len(args) < 2:
        return "Enter name and new address: edit-address Name New Address"

    name = args[0]
    new_address = " ".join(args[1:])

    record_list = book.find(name)
    record = record_list[0] if record_list else None

    if not record:
        return f"Contact with name '{name}' not found."

    record.edit_address(new_address)
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
    console = Console()

    if not notebook.notes:
        console.print("[yellow]No notes available.[/yellow]")

    sorted_notes = notebook.sort_notes_by_tag()
    table = Table(title="🗂️ Sorted Notes by Tag", title_style="bold magenta")

    table.add_column("№", style="dim", justify="center")
    table.add_column("Title", style="bold green")
    table.add_column("Tags", style="yellow")
    table.add_column("Text", style="white")

    for idx, note in enumerate(sorted_notes, start=1):
        tags = ", ".join(note.tags) if note.tags else "no tags"
        table.add_row(str(idx), note.title, tags, note.text)

    console.print(table)
    return ""

# ==================ФУНКЦІЯ ДЛЯ ПОШУКУ СХОЖИХ КОМАНД================================
@input_error
def suggest_command(user_input: str) -> str | None:
    matches = difflib.get_close_matches(user_input, KNOWN_COMMANDS, n=1, cutoff=0.6)
    return matches[0] if matches else None

def find_notes_by_tag(args: list, notebook: Notebook) -> str:
    console = Console()

    if not args:
        return "[red]Please provide a tag to search for.[/red]"

    tag_to_find = args[0].lower()

    found_notes = [note for note in notebook.notes if tag_to_find in [tag.lower() for tag in note.tags]]

    if not found_notes:
        return f"[yellow]No notes found with tag: '{tag_to_find}'[/yellow]"

    table = Table(title=f"🔎 Notes with Tag: '{tag_to_find}'", title_style="bold cyan")
    table.add_column("№", style="dim", justify="center")
    table.add_column("Title", style="bold green")
    table.add_column("Tags", style="yellow")
    table.add_column("Text", style="white")

    for idx, note in enumerate(found_notes, start=1):
        tags = ", ".join(note.tags) if note.tags else "no tags"
        table.add_row(str(idx), note.title, tags, note.text)

    console.print(table)
    return ""
