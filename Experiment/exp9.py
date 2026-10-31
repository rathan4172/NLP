import re

text = "The cat runs quickly"
words = text.split()

patterns = [
    (r"The|A|An", "Determiner"),
    (r".*ly$", "Adverb"),
    (r".*s$", "Verb"),
    (r".*", "Noun")
]

print("Rule-Based POS Tags:")

for word in words:
    for pattern, tag in patterns:
        if re.fullmatch(pattern, word, re.IGNORECASE):
            print(word, ":", tag)
            break
