def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Неправильне значення."
        except KeyError:
            return "Контакт не знайдено."
        except IndexError:
            return "Недостатньо аргументів."
    return wrapper
