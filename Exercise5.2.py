# Initialize an empty list to store numbers.
numbers = []

# Continuously prompt the user for input.
while True:
    # Prompt the user to enter a number.
    user_input = input("Enter a number: ")
    
    # If the user inputs 'done', exit the loop.
    if user_input == 'done':
        break
    
    try:
        # Attempt to convert the user input to an integer.
        number = int(user_input)
        # Add the valid integer to the list.
        numbers.append(number)
        
    except ValueError:
        # Handle the case where the input is not a valid integer.
        print("Invalid input.")

# After exiting the loop, find the largest number in the list.
largest = max(numbers)
# Find the smallest number in the list.
smallest = min(numbers)

# Print the largest number.
print("Maximum is", largest)
# Print the smallest number.
print("Minimum is", smallest)