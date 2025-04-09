from cli.parser import parse_command
from cli.decorators import input_error
from cli.commands import (
    add_contact, change_contact, phone_username, show_all_contacts,
    add_birthday, show_birthday, birthdays, delete_contact,
    add_note, delete_note, search_notes,
)
"""
закоментовано команди, які мають бути реалізовані пізніше в рамках додаткового завдання: tag_note, sort_notes_by_tag, analyze_input
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
        elif command == "phone":
            print(phone_username(args, book))
        elif command == "all":
            print(show_all_contacts(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        elif command == "delete":
            print(delete_contact(args, book))
        elif command == "add-note":
            print(add_note(args, notebook))
        elif command == "delete-note":
            print(delete_note(args, notebook))
        elif command == "search-note":
            print(search_notes(args, notebook))
 #       elif command == "tag-note":
 #           print(tag_note(args, book, notebook))
 #       elif command == "sort-notes-by-tag":
 #           print(sort_notes_by_tag(args, book, notebook))
 #       elif command == "analyze": 
 #           print(analyze_input(args, book, notebook))
        else:
            print("Invalid command.")
