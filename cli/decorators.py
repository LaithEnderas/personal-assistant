from cli.rich_table import print_message

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError as e:
            print_message(str(e) or "Неправильне значення.", style="bold red", title="⚠️ Force Disturbance")

        except KeyError as e:
            print_message(str(e) or "Контакт не знайдено.", style="bold red", title="🛸 Missing Contact")

        except IndexError as e:
            print_message(str(e) or "Недостатньо аргументів.", style="bold red", title="📦 Missing Data")

        except NameError as e:
            print_message(
                "Looks like something important wasn't defined... Is your code missing a variable or is your command incomplete?",
                style="bold red", title="💥 Critical Failure in the Code Matrix")

        except Exception as e:
            print_message(
                "Wokie encountered an unknown galactic anomaly.\n"
                f"[dim]({type(e).__name__}: {e})[/dim]",
                style="bold red", title="💫 Unexpected Disturbance in the Force")

    return wrapper
