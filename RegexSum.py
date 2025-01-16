import re

# Read the content of the file.
with open('regex_sum_2056821.txt', 'r') as file:
    content = file.read()  # Read the entire content as a single string.

# Use a raw string for the regex pattern to find all sequences of digits.
matches = re.findall(r'[0-9]+', content)

count_values = len(matches)  # Count how many numeric values were found.
total_sum = sum(int(match) for match in matches)  # Calculate the sum of the integer values.

# Output the result with a clear message.
print(f'There are {count_values} values and the sum is {total_sum}.')