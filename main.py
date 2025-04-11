from storage.file_io import load_data, save_data
from cli.loop import command_loop
from cli.banner import show_welcome_banner


def main():
    book, notebook = load_data()
    show_welcome_banner() 
    try:
        command_loop(book, notebook)
    finally:
        save_data(book, notebook)
        print("Good bye!")

if __name__ == "__main__":
    main()
