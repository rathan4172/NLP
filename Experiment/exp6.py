import random

text = "I love NLP. I love Python. Python is interesting."
words = text.replace(".", "").split()

bigrams = {}
for i in range(len(words) - 1):
    bigrams.setdefault(words[i], []).append(words[i + 1])

word = "I"
result = [word]

for i in range(6):
    if word in bigrams:
        word = random.choice(bigrams[word])
        result.append(word)
    else:
        break

print("Generated Text:", " ".join(result))
