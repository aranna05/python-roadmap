## 1. solve no 1

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")



## 2. solve no 2

score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")



## 3. solve no 3

age = int(input("Enter your age: "))
license = input("Do you have a license? (yes/no): ")

if age < 18:
    print("Too young to drive.")
elif age >= 18 and license == "yes":
    print("You are eligible to drive.")
else:
    print("You must have a license to drive.")



## 4. solve no 4

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter city name: ").lower()

if city in india:
    print("City belongs to India")
elif city in pakistan:
    print("City belongs to Pakistan")
elif city in bangladesh:
    print("City belongs to Bangladesh")
else:
    print("City not found")



## 5. solve no 5

city1 = input("Enter first city: ").lower()
city2 = input("Enter second city: ").lower()

if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in Pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")



## 6. solve no 6

sugar = int(input("Enter your fasting sugar level: "))

if sugar < 80:
    print("Sugar level is low")
elif sugar > 100:
    print("Sugar level is high")
else:
    print("Sugar level is normal")

