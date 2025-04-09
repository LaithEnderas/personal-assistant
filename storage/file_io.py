import pickle
import os
from models.address_book import AddressBook
from models.note import Notebook

DATA_FILE = "data.pkl"

def save_data(book: AddressBook, notebook: Notebook, filename: str = DATA_FILE):
    data = {
        "book": book,
        "notebook": notebook
    }
    try:
        with open(filename, "wb") as file:
            pickle.dump(data, file)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data(filename: str = DATA_FILE):
    if os.path.exists(filename):
        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
                book = data.get("book", AddressBook())
                notebook = data.get("notebook", Notebook())
                print("Data loaded successfully.")
                return book, notebook
        except Exception as e:
            print(f"Error loading data: {e}")

    print("New address book and notebook created.")
    return AddressBook(), Notebook()
