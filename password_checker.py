# Password Strength Checker
# Project 1 - Cyber Security
# DecodeLabs

password = input("Enter your password: ")

# Checks
has_min_length = len(password) >= 8
has_uppercase = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

# Calculate score
score = 0

if has_min_length:
    score += 1

if has_uppercase:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1

# Determine password strength
if score <= 1:
    strength = "Weak Password"
elif score <= 3:
    strength = "Medium Password"
else:
    strength = "Strong Password"

# Display results
print("\n----- Password Analysis -----")
print(f"Password Length: {len(password)}")
print(f"Contains Uppercase: {has_uppercase}")
print(f"Contains Number: {has_digit}")
print(f"Contains Symbol: {has_symbol}")
print(f"Password Strength: {strength}")
