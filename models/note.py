class Note:
    """Одна нотатка. Містить текст і список тегів."""
    def __init__(self, text, tags=None):
        self.text = text
        self.tags = tags if tags else []


class Notebook:
    """Колекція нотаток. Додавання, пошук, видалення."""
    def __init__(self):
        self.notes = []
