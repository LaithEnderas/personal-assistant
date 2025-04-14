from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

def show_command_table():
    table = Table(title="[bold magenta]🛸 Wokie Command Guide - Use the Force, User![/bold magenta]")

    table.add_column("№", style="cyan", justify="center")
    table.add_column("Command", style="bold green")
    table.add_column("Arguments (example)", style="yellow")
    table.add_column("Functionality", style="white")

    commands = [
        ("1", "add", "Name 0123456789", "Add new contact or phone"),
        ("2", "change", "Name old_phone new_phone", "Change contact's phone"),
        ("3", "search", "Name or keyword", "Find contact by name or detail"),
        ("4", "all", "-", "Show all contacts"),
        ("5", "add-birthday", "Name 01.01.2000", "Add birthday to contact"),
        ("6", "show-birthday", "Name", "Show birthday of contact"),
        ("7", "birthdays", "10", "Upcoming birthdays (default 7 days)"),
        ("8", "delete", "Name", "Delete contact"),
        ("9", "add-note", "Title Text", "Add note with title and text"),
        ("10", "edit-note", "Title New text", "Edit note text"),
        ("11", "delete-note", "Title", "Delete note by title"),
        ("12", "search-note", "Keyword", "Search note by keyword"),
        ("13", "add-email", "Name email@example.com", "Add email to contact"),
        ("14", "edit-email", "Name old new", "Edit contact's email"),
        ("15", "add-address", "Name Street 123", "Add address to contact"),
        ("16", "edit-address", "Name Old New", "Edit contact's address"),
        ("17", "add-tag", "Title Tag", "Add tag to note"),
        ("18", "sort-notes-by-tag", "-", "Sort and show notes by tag"),
        ("19", "hello", "-", "Get a greeting from Wokie"),
        ("20", "close / exit", "-", "End the session"),
        ("21", "help", "-", "Show commands table"),
    ]

    for row in commands:
        table.add_row(*row)

    console.print(table)

def print_message(message: str, style: str = "bold yellow", title: str = None):
    title = title or "📡 Message from Wokie"

    panel = Panel(
        Align.left(Text(message, style=style)),  
        title=title,
        title_align="left",
        border_style=style,
        expand=False, 
        padding=(0, 1)
    )
    console.print(panel)