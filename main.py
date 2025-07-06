import string
text = input("Введіть рядок: ")
size = 140
text = text.lower()
text = "#" + text
text = text.title()
for char in string.punctuation:
    if char in text:
        text = text.replace(char,"")
text = text.replace(" ", '')
print(text[:size])