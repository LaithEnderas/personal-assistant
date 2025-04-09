from cli.parser import parse_command
from cli.decorators import input_error
from cli.commands import (
    add_contact, change_contact, search_contacts, show_all_contacts,
    add_birthday, show_birthday, birthdays, delete_contact,
    add_note, delete_note, search_notes,
    add_email, edit_email, add_address, edit_address,
    add_tag, sort_notes_by_tag, search_by_tag  
)

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
        elif command == "add_birthday":
            print(add_birthday(args, book))
        elif command == "show_birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            days = int(args[0]) if args else 7
            print(birthdays(book, days))
        elif command == "delete":
            print(delete_contact(args, book))
        elif command == "add_note":
            print(add_note(args, notebook))
        elif command == "delete_note":
            print(delete_note(args, notebook))
        elif command == "search_notes":
            print(search_notes(args, notebook))
        elif command == "add_email":
            print(add_email(args, book))
        elif command == "edit_email":
            print(edit_email(args, book))
        elif command == "add_address":
            print(add_address(args, book))
        elif command == "edit_address":
            print(edit_address(args, book))
        elif command == "add_tag":
            print(add_tag(args, notebook))  
        elif command == "search_by_tag":
            print(search_by_tag(args, notebook))  
        elif command == "sort_notes_by_tag":
            print(sort_notes_by_tag(notebook))  
#       elif command == "analyze_input":
#           print(analyze_input(args, book, notebook))
        else:
            print("Invalid command.")


