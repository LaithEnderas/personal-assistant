from cli.parser import parse_command
from cli.decorators import input_error
from cli.commands import (
    add_contact, change_contact, phone_username,
    add_birthday, show_birthday, birthdays, show_all_contacts
)

@input_error
def command_loop(book):
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
        else:
            print("Invalid command.")
