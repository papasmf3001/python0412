import re

# Define a regular expression pattern to match an email address
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Define a string to search for the pattern
string = "My email address is kim@gmail.com"

# Use the search() function of the re module to find the first match of the pattern in the string
match = re.search(pattern, string)

# Check if a match was found
if match:
    # Print the matched substring
    print("Found an email address:", match.group(0))
else:
    # Print a message if no match was found
    print("No email address found in the string.")
