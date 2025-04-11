from cli.parser import parse_command
from cli.decorators import input_error
from cli.commands import (
    add_contact, change_contact, search_contacts, show_all_contacts,
    add_birthday, show_birthday, birthdays, delete_contact,
    add_note, delete_note, search_notes, add_email, change_email, add_address, edit_address, add_tag, sort_notes_by_tag, edit_note, suggest_command, help_command,
)
from models.note import (Note, Notebook)
from rich.console import Console
"""
Закоментовано команди, які мають бути реалізовані пізніше в рамках додаткового завдання:
add_tag, sort_notes_by_tag, analyze_input
"""
console = Console()
@input_error
def command_loop(book, notebook):
    while True:
        user_input = console.input("[bold cyan]Enter a command:[/bold cyan] ")
        command, args = parse_command(user_input)

        if command in ["close", "exit"]:
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "search":
            print(search_contacts(args, book))
        elif command == "all":
            print(show_all_contacts(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            result = birthdays(args, book)
            if result:
                print(result)
        elif command == "delete":
            print(delete_contact(args, book))
        elif command == "add-note":
            print(add_note(args, notebook))
        elif command == "edit-note":
            print(edit_note(args, notebook))
        elif command == "delete-note":
            print(delete_note(args, notebook))
        elif command == "search-note":
            print(search_notes(args, notebook))
        elif command == "add-email":
            print(add_email(args, book))
        elif command == "edit-email":
            print(change_email(args, book))
        elif command == "add-address":
            print(add_address(args, book))
        elif command == "edit-address":
            print(edit_address(args, book)) 
        elif command == "add-tag":
          print(add_tag(args, notebook))
        elif command == "sort-notes-by-tag":
           print(sort_notes_by_tag(args, notebook))
        elif command == "help":
           print(help_command())
        else:
            suggestion = suggest_command(command)
            if suggestion:
                print(f"Did you mean '{suggestion}'?")
            else:
                print("Invalid command.")
