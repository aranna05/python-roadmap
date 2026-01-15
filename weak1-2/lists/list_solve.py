
## level 1..............................................................................................................................
## solve no 1

marks = [70, 65, 80, 75, 90]
total = sum(marks)
print(total)


## solve no 2

ages = [12, 18, 25, 10, 30]

count = 0
for age in ages:
    if age > 18:
        count += 1

print(count)


## solve no 3

fruits = ["apple", "banana", "mango"]

print("banana" in fruits)


## solve no 4

numbers = [10, 20, 30, 40]
numbers.pop()
print(numbers)


## solve no 5

prices = [250, 100, 450, 300]
prices.sort()
print(prices)


## level 2..............................................................................................................................
## solve no 1

numbers = [1,2,3,4,5,6,7,8]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)


## solve no 2

marks = [55, 78, 90, 32, 67]

print(max(marks))
print(min(marks))


## solve no 3

items = ['pen','pencil','eraser','sharpener']

index = items.index('pencil')
items.insert(index + 1, 'scale')

print(items)



## solve no 4

numbers = [1,2,2,3,4,4,5]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)


## solve no 5

data = [10, 20, 30, 40]
data.reverse()
print(data)
