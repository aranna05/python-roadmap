## solve no 1

street = "123 Maple Ave"
city = "London"
country = "UK"

# Method 1: Using + operator
address_plus = street + "\n" + city + "\n" + country

# Method 2: Using f-string (Preferred in modern Python)
address_f = f"{street}\n{city}\n{country}"

print("--- Address Output ---")
print(address_f)


## solve no 2

sentence = "Earth revolves around the sun"

# 1. Print "revolves" (starts at index 6, ends before 14)
print(sentence[6:14])

# 2. Print "sun" using negative index
print(sentence[-3:])


## solve no 3

veggies = 3
fruits = 2

print(f"I eat {veggies} veggies and {fruits} fruits daily.")



## solve no 4

s = 'maine 200 banana khaye'

# One-line replacement
s = s.replace('200', '10').replace('banana', 'samosa')

print(s)

