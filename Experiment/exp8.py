text = "Dogs run fast"
words = text.split()

probabilities = {
    "Dogs": {"Noun": 0.9, "Verb": 0.1},
    "run": {"Verb": 0.8, "Noun": 0.2},
    "fast": {"Adverb": 0.7, "Adjective": 0.3}
}

print("Stochastic POS Tags:")

for word in words:
    tag = max(probabilities[word], key=probabilities[word].get)
    print(word, ":", tag)
