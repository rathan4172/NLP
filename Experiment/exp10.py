words = ["The", "dogs", "bark"]
tags = ["Noun", "Noun", "Noun"]

print("Initial Tags:")
print(list(zip(words, tags)))

# Transformation rule: The is a determiner
for i, word in enumerate(words):
    if word.lower() == "the":
        tags[i] = "Determiner"

# Transformation rule: bark after a noun is a verb
for i in range(1, len(words)):
    if words[i].lower() == "bark" and tags[i - 1] == "Noun":
        tags[i] = "Verb"

print("Final Tags:")
print(list(zip(words, tags)))
