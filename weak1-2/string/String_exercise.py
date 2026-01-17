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



