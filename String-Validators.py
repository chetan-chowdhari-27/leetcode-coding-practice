# Input
s = input()

# Output the required checks
print(any(c.isalnum() for c in s))     # Checks if any alphanumeric characters
print(any(c.isalpha() for c in s))     # Checks if any alphabetical characters
print(any(c.isdigit() for c in s))     # Checks if any digits
print(any(c.islower() for c in s))     # Checks if any lowercase characters
print(any(c.isupper() for c in s))     # Checks if any uppercase characters
