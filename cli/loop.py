from cli.parser import parse_command
from cli.decorators import input_error
from cli.commands import (
    add_contact, change_contact, search_contacts, show_all_contacts, add_tag, sort_notes_by_tag,
    add_birthday, show_birthday, birthdays, delete_contact,
    add_note, delete_note, search_notes, add_email, edit_email, add_address, edit_address
)
"""
Закоментовано команди, які мають бути реалізовані пізніше в рамках додаткового завдання: analyze_input
"""

@input_error
def command_loop(book, notebook):
    while True:
        user_input = input("Enter a command: ")
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
            days = int(args[0]) if args else 7
            print(birthdays(book, days))
        elif command == "delete":
            print(delete_contact(args, book))
        elif command == "add-note":
            print(add_note(args, notebook))
        elif command == "delete-note":
            print(delete_note(args, notebook))
        elif command == "search-note":
            print(search_notes(args, notebook))
        elif command == "add-email":
            print(add_email(args, book))
        elif command == "edit-email":
            print(edit_email(args, book))
        elif command == "add-address":
            print(add_address(args, book))
        elif command == "edit-address":
            print(edit_address(args, book))     
       elif command == "add_tag":
           print(add_tag(args, book, notebook))
       elif command == "sort-notes-by-tag":
           print(sort_notes_by_tag(args, book, notebook))
#       elif command == "analyze":
#           print(analyze_input(args, book, notebook))
        else:
            print("Invalid command.")
