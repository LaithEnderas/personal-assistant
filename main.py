from storage.file_io import load_data, save_data
from cli.loop import command_loop

def main():
    book, notebook = load_data()
    try:
        command_loop(book, notebook)
    finally:
        save_data(book)
        print("Good bye!")

if __name__ == "__main__":
    main()
