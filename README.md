#  Wokie — Terminal Assistant for Contacts and Notes

**Wokie** is a multifunctional terminal assistant styled in the spirit of *Star Wars*. It helps you manage contacts and notes efficiently with a smart CLI and visual terminal interface.

---

##  Features

###  Contacts
- Add new contacts and phone numbers  
- Edit and remove phone numbers  
- Add/edit email addresses, birthdays, and physical addresses  
- View all contacts in a table  
- Search by name, phone, email, address, or birthday  
- Show upcoming birthdays within a chosen number of days  

###  Notes
- Create and delete notes by title  
- Edit note content  
- Search by keywords in title or body  
- Add and remove tags  
- Sort and filter notes by tags  

###  Smart CLI
- Fuzzy matching for mistyped commands  
- `help` command with a complete table of available actions  
- Rich terminal interface via the `rich` library  
- Welcome banner on launch  
- Styled messages, hints, and error feedback  

---

##  Installation & Launch

1. Clone the repository:

```bash
git clone https://github.com/yourname/wokie-assistant.git
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the assistant:

```bash
python main.py
```

---

##  Command Reference

| Command               | Arguments                     | Description                            |
|----------------------|-------------------------------|----------------------------------------|
| `add`                | Name Phone                    | Add a new contact or phone number      |
| `change`             | Name OldPhone NewPhone        | Edit existing phone number             |
| `delete`             | Name                          | Delete a contact                       |
| `search`             | Keyword                       | Search contacts                        |
| `all`                | —                             | Show all contacts                      |
| `add-birthday`       | Name DD.MM.YYYY               | Add birthday to a contact              |
| `show-birthday`      | Name                          | Show contact's birthday                |
| `birthdays`          | N (days)                      | Show upcoming birthdays                |
| `add-email`          | Name Email                    | Add email to a contact                 |
| `edit-email`         | Name OldEmail NewEmail        | Edit email                             |
| `add-address`        | Name Address                  | Add address to a contact               |
| `edit-address`       | Name NewAddress               | Edit address                           |
| `add-note`           | Title Text                    | Add a note                             |
| `edit-note`          | Title NewText                 | Edit note                              |
| `delete-note`        | Title                         | Delete note                            |
| `search-note`        | Keyword                       | Search notes                           |
| `add-tag`            | Title Tag                     | Add tag to a note                      |
| `search-by-tag`      | Tag                           | Find notes with a specific tag         |
| `sort-notes-by-tag`  | —                             | Show notes sorted by tags              |
| `hello`              | —                             | Greet the assistant                    |
| `help`               | —                             | Show available commands                |
| `exit / close`       | —                             | Exit the assistant                     |

---

##  Project Structure

```
personal-assistant/
│
├── cli/
│   ├── banner.py
│   ├── commands.py
│   ├── decorators.py
│   ├── loop.py
│   ├── parser.py
│   └── rich_table.py
│
├── models/
│   ├── address_book.py
│   ├── fields.py
│   ├── note.py
│   └── record.py
│
├── storage/
│   └── file_io.py
│
├── main.py
└── README.md
```

---

##  Authors

- Bohdan - Team Lead
- Oleksandr  
- Alina  
- Iryna  
