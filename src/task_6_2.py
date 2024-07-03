import re

text = 'Позвоните мне по номеру 555-123-4567 или 555-987-6543'

pattern = re.compile(r'\(?\d[-\)]?\d[-\)]?\d[-\)]?\d[-\)]?\d[-\)]?\d[-\)]?\d[-\)]?\d[-\)]?\d[-\)]?\d')

matches = pattern.finditer(text)

for match in matches:
    print(match)
