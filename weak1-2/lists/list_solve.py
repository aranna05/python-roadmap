
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


## Advance level.....................................................................................................................

#### 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

exp = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:",exp[1]-exp[0]) # 150

# 2. Find out your total expense in first quarter (first three months) of the year
print("Expense for first quarter:",exp[0]+exp[1]+exp[2]) # 7150

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in exp) # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Expenses at the end of June:",exp) # [2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp) # [2200, 2350, 2600, 1930, 2190, 1980]




#### 2. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this list

heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)
# 5. Sort the list in alphabetical order
heros.sort()
print(heros)
