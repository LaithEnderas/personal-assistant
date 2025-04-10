from storage.file_io import load_data, save_data
from cli.loop import command_loop

def main():
    book, notebook = load_data()
    print('''
          Please use the following commands to interact with Wokie

          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          |     Command Name        |        Arguments (examples)           |                         Functionality                                                 |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 1.  add                 |  Name 0123456789                      | adds a New contact or adds a Phone to existing contact by a specified contact's Name  |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 2.  change              |  Name 0987654321 0501234567           | changes an Old phone to a New phone for a specified contact's Name                    |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 3.  search              |  Name or Keyword                      | finds a List of contacts by a specified contact's Name or other Keyword               |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 4.  all                 |  NO ARGUMENTS                         | shows all Contacts already added to Address book                                      |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 5.  add-birthday        |  Name 01.01.2000                      | adds a Birthday for specified contact's Name                                          |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 6.  show-birthday       |  Name                                 | shows a Birthday for specified contact's Name                                         |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          |                         |                                       | shows a list of Contacts whose Birthdays are to come during a specified number of days|
          | 7.  birthdays           |  10                                   |  - if not specified - 7 days by default                                               |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 8.  delete              |  Name                                 | removes a Contact from Address book by a specified contact's Name                     |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 9.  add-note            |  Title Text                           | adds a Note to Notebook with specified note's Title and Text                          |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 10. edit-note           |  Title Updated text                   | edits note's Text for a specified Title                                               |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 11. delete-note         |  Title                                | removes a Note from Notebook by a specified note's Title                              |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 12. search-note         |  Keyword                              | finds a Note by a specified Keyword                                                   |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 13. add-email           |  Name email@example.com               | adds an Email for specified contact's Name                                            |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 14. edit-email          |  Name old@example.com new@example.com | changes an Old email to a New email for a specified contact's Name                    |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 15. add-address         |  Name Some Street 123                 | adds an Address for specified contact's Name                                          |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 16. edit-address        |  Name Old St 1 New St 2               | changes an Old address to a New address for a specified contact's Name                |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 17. add-tag             |  Title Tag                            | adds a Tag for a specified note's Title                                               |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 18. sort-notes-by-tag   |  NO ARGUMENTS                         | shows all Notes sorted by Tags                                                        |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 19. hello               |  NO ARGUMENTS                         | gives a greeting \"How can I help you?\"                                                |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          | 20. close or exit       |  NO ARGUMENTS                         | finishes the interaction with Wokie                                                   |
          |-------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
          ''')   
    try:
        command_loop(book, notebook)
    finally:
        save_data(book, notebook)
        print("Good bye!")

if __name__ == "__main__":
    main()
