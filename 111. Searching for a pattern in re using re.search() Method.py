import re
pattern = r"expression"		# Define a regular expression pattern
text = "Hello, world!" 		# Match the pattern against a string
match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")

