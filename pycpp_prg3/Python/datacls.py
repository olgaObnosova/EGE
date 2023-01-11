from dataclasses import dataclass

@dataclass
class TBook:
  author: str = "?"
  title: str = ""
  count: int = 0

b = TBook("Author", "Title")
print(b)
b = TBook("Author", "Title", 12)
print(b)
    
