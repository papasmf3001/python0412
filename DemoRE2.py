import re

# Define a regular expression pattern to match a 4-digit year
pattern = r"\b\d{4}\b"

# Define a string to search for the pattern
string = "The year 2023 is almost here, but 2022 is still fresh in our memories."

# Use the search() function of the re module to find the first match of the pattern in the string
match = re.search(pattern, string)

# Check if a match was found
if match:
    # Print the matched substring
    print("Found a 4-digit year:", match.group(0))
else:
    # Print a message if no match was found
    print("No 4-digit year found in the string.")
