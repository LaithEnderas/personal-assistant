# Personal Assistant

A command-line assistant application designed to help manage contacts and notes efficiently.

## Features

### Contact Book

- Add new contacts with name and phone number
- Edit or change existing phone numbers
- Delete contacts
- Add, edit, or delete emails and addresses
- Add and view birthdays
- Search contacts by any field
- Show all contacts
- Display upcoming birthdays in the next _n_ days

### Notebook

- Add and delete notes with title and body text
- Search notes by keywords
- Add tags to notes
- Search and sort notes by tags

### Extra Features

- Fuzzy command matching: bot will guess user intent for incorrect or partial commands
- Modular design: easily extendable and testable structure

## Technologies

- Python 3.10+
- Built-in libraries:
  - dataclasses
  - pickle
  - os
  - difflib

## How to Run

1. Clone or download this repository
2. Run the assistant:

```
python main.py
```

## Commands Reference

| Command                        | Description                                 |
|-------------------------------|---------------------------------------------|
| `add Name 0123456789`         | Add a new contact                           |
| `change Name old new`         | Change a phone number                       |
| `delete Name`                 | Delete a contact                            |
| `search keyword`              | Search contacts                             |
| `add-birthday Name 01.01.2000`| Add birthday to contact                     |
| `birthdays 7`                 | Show upcoming birthdays in the next 7 days  |
| `add-note Title Body`         | Add a new note                              |
| `delete-note Title`           | Delete a note by title                      |
| `search-note keyword`         | Search notes by keyword                     |
| `add-tag Title TagName`       | Add a tag to a note                         |
| `search-by-tag TagName`       | Search notes by tag                         |
| `sort-notes-by-tag`           | Sort notes by assigned tags                 |
| `exit` or `close`             | Exit the assistant                          |

## Project Structure

```
personal-assistant/
│
├── cli/
│   ├── commands.py
│   ├── loop.py
│   └── parser.py
│
├── models/
│   ├── address_book.py
│   ├── note.py
│   └── record.py
│
├── storage/
│   └── file_io.py
│
├── main.py
└── README.md
```

## Team Members

- Team Lead: Bohdan
- Developers: Oleksandr, Alina, Iryna
