from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "playing",
    "played",
    "running",
    "happiness",
    "studies",
    "connected",
    "computational"
]

print("Porter Stemming Results:")

for word in words:
    print(word, "->", ps.stem(word))
