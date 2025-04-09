from dataclasses import dataclass, field


@dataclass
class Note:
    title: str
    text: str
    tags: list[str] = field(default_factory=list)

    def __str__(self):
        tags_formatted = ", ".join(self.tags) if self.tags else "no tags"
        return f"Title: {self.title}\nNote: {self.text}\nTags: {tags_formatted}"     # Покищо базове форматування вигляду нотатки

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)

    def edit_text(self, new_text: str):
        self.text = new_text


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note: Note):
        if any(existing.title == note.title for existing in self.notes):
            return None
        self.notes.append(note)
        return note

    def search_notes(self, query: str):
        return [
        note for note in self.notes
        if query.lower() in note.title.lower() or query.lower() in note.text.lower()
    ]

    def delete_note(self, title: str):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return note
        return None

    def edit_note(self, title: str, new_text: str):
        for note in self.notes:
            if note.title == title:
                note.edit_text(new_text)
                return note
        return None

    def find_by_tag(self, tag: str):
        return [note for note in self.notes if tag in note.tags]

    def sort_notes_by_tag(self):
        return sorted(self.notes, key=lambda note: note.tags)