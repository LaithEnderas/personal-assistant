from storage.file_io import load_data, save_data
from cli.commands import command_loop

def main():
    book = load_data()
    try:
        command_loop(book)
    finally:
        save_data(book)
        print("Good bye!")

if __name__ == "__main__":
    main()
