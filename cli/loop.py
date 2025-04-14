from cli.parser import parse_command
from cli.decorators import input_error
from cli.commands import (
    add_contact, change_contact, search_contacts, show_all_contacts,
    add_birthday, show_birthday, birthdays, delete_contact,
    add_note, delete_note, search_notes, add_email, change_email,
    add_address, edit_address, add_tag, sort_notes_by_tag, edit_note,
    suggest_command, help_command, find_notes_by_tag
)
from cli.rich_table import print_message
from models.note import Note, Notebook
from rich.console import Console
from rich.text import Text

console = Console()

@input_error
def command_loop(book, notebook):
    while True:
        user_input = console.input("[bold cyan]Enter a command:[/bold cyan] ")
        command, args = parse_command(user_input)

        if command in ["close", "exit"]:
            print_message("Session ended. May the data be with you!", style="bold green", title="👋 Farewell")
            break

        elif command == "hello":
            print_message("How can I help you, Jedi?", style="bold blue", title="🤖 Wookiee Ready")

        elif command == "add":
            result = add_contact(args, book)
            if result:
                print_message(result, style="bold green", title="✅ Contact Added")

        elif command == "change":
            result = change_contact(args, book)
            if result:
                print_message(result, style="bold green", title="🔁 Contact Updated")

        elif command == "search":
            result = search_contacts(args, book)
            if result:
                print_message(result, style="bold yellow", title="🔍 Search")

        elif command == "all":
            show_all_contacts(book)

        elif command == "add-birthday":
            result = add_birthday(args, book)
            if result:
                if "added" in result.lower():
                    print_message(result, style="bold green", title=":birthday: Birthday Set")
                else:
                    print_message(result, style="bold red", title=":birthday: Birthday Set")

        elif command == "show-birthday":
            result = show_birthday(args, book)
            if result:
                print_message(result, style="bold cyan", title="🎉 Birthday")

        elif command == "birthdays":
            result = birthdays(args, book)
            if result:
                print_message(result, style="bold magenta", title="📅 Birthdays")

        elif command == "delete":
            result = delete_contact(args, book)
            if result:
                print_message(result, style="bold red", title="🗑️ Contact Deleted")

        elif command == "add-note":
            result = add_note(args, notebook)
            if result:
                print_message(result, style="bold green", title="📝 Note Added")

        elif command == "edit-note":
            result = edit_note(args, notebook)
            if result:
                print_message(result, style="bold yellow", title="✏️ Note Updated")

        elif command == "delete-note":
            result = delete_note(args, notebook)
            if result:
                print_message(result, style="bold red", title="🗑️ Note Deleted")

        elif command == "search-note":
            search_notes(args, notebook)

        elif command == "add-email":
            result = add_email(args, book)
            if result:
                print_message(result, style="bold green", title="📧 Email Added")

        elif command == "edit-email":
            result = change_email(args, book)
            if result:
                print_message(result, style="bold yellow", title="✉️ Email Updated")

        elif command == "add-address":
            result = add_address(args, book)
            if result:
                print_message(result, style="bold green", title="📍 Address Added")

        elif command == "edit-address":
            result = edit_address(args, book)
            if result:
                print_message(result, style="bold yellow", title="📌 Address Updated")

        elif command == "add-tag":
            result = add_tag(args, notebook)
            if result:
                print_message(result, style="bold green", title="🏷️ Tag Added")

        elif command == "sort-notes-by-tag":
            sort_notes_by_tag(args, notebook)

        elif command == "search-by-tag":
            result = find_notes_by_tag(args, notebook)
            if result:
                print_message(Text.from_markup(result), style="bold yellow", title="🔍 Search")

        elif command == "help":
            help_command()

        else:
            suggestion = suggest_command(command)
            if suggestion:
                message = Text.from_markup(f"Did you mean [bold green]{suggestion}[/bold green]?")
                print_message(message, style="yellow", title="🤔 Unrecognized Command")
            else:
                message = Text.from_markup("Invalid command. Type [bold]help[/bold] to see the list.")
                print_message(message, style="yellow", title="❌ Unknown Transmission")

