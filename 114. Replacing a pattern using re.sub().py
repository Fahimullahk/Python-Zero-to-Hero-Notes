import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."

new_text = re.sub(pattern, "dog", text)

print(new_text)

