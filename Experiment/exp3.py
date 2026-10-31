import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays", "running", "runs", "happily"]

print("Morphological Analysis:")

for word in words:
    root = stemmer.stem(word)
    print(word, "->", root)
