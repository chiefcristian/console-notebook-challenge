# TODO: Agrega el código de las clases de la interfaz de usuario aquí. Borra este comentario al terminar.
from datetime import datetime
class Note:
    HIGH:str="HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

def __init__(self, code: str, title: str, text: str, importance: str):
    self.code = code
    self.title = title
    self.text = text
    self.importance = importance
    self.creation_date: datetime = datetime.now()
    self.tags: list[str] = []
def add_tag(self, tag: str):
    if tag not in self.tags:
        self.tags.append(tag)
def _str_(self):
    return f"Date: {self.creation_date}\n{self.title}: {self.text}"

class Notebook:
    def _init_(self):
        self.notes: list[Note] = []

    def add_note(self, title: str, text: str, importance: str) -> Note:
        new_code = {len(self.notes)}
        while new_code not in self.notes:
            new_code += 1
        new_note = Note(new_code, title, text, importance)
        self.notes.append(new_note)
        return new_note
    def delete_note(self, code:int):
        self.notes = [note for note in self.notes if note.code != code]

    def important_notes(self) -> List[Note]:
        return [note for note in self.notes if note.importance in ("HIGH", "MEDIUM")]

    def notes_by_tag(self, tag: str) -> List[Note]:
        return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self) -> str:
        tag_count = Counter(tag for note in self.notes for tag in note.tags)
        if not tag_count:
            return ""
        max_count = max(tag_count.values())
        most_common_tags = [tag for tag, count in tag_count.items() if count == max_count]
        return min(most_common_tags)

