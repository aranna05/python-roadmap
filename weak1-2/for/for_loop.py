## solve no 1
count= 0
for x in range(1,10):
    if(x%2==0):
        print(x)
        count+=1
print (f"we have {count} even numbers")


## solve no 2
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0

for iteam in result:
    if iteam == "heads":
        count += 1
print(count)


## solve no 3
for x in range(1, 10):
    if (x % 2 == 0):
        continue
    print(x * x)


## solve no 4
months = ['January', 'February', 'March', 'April', 'May']
expense_list = [2540, 2510, 2100, 3100, 2880]

expense = int(input("Enter the expense amount to search for: "))

for x in range(len(expense_list)):
    if expense == expense_list[x]:
        print(f"Expense of {expense} found in {months[x]}.")
        break

else: 
    print(f"Expense of {expense} not found in the list.")



## solve no 5
for km in range(1, 6):
    tired = input(f"After {km} km, are you tired? (yes/no): ")

    if tired.lower() == "yes":
        print("You didn't finish the race")
        break
else:
    print("Congratulations! You finished the race")



## solve no 6
for x in range (1, 6):
    print("*" * x) 
