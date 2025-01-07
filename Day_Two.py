from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Ask for user input
name = input("What is your name? ")
age = int(input("How old are you? "))

# Calculate the year of birth
year_of_birth = current_year - age

# Print the greeting and year of birth
print(f"Hello, {name}! You were born in {year_of_birth}.")
