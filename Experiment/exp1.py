import re

text = "Python is a programming language. Python is easy to learn."

match = re.match("Python", text)
search = re.search("programming", text)
find = re.findall("Python", text)

print("Match:", match.group() if match else "Not Found")
print("Search:", search.group() if search else "Not Found")
print("Find All:", find)
