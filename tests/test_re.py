import re

text = "@Your input text here!"
text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

print(text)  # your input text here