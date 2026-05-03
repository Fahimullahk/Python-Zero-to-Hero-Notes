import re
pattern = r"cat"
text = "The cat is in the hat."
matches = re.findall(pattern, text)
print(matches)

