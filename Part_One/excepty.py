try:
    user_age = int(input("Enter your age: "))
    income = 10000
    risk = income / user_age
    print(f"Your risk factor is: {risk}")
except ZeroDivisionError:
    print("Age cannot be zero. Please enter a valid age.")

except ValueError:
    print("Invalid input. Please enter a number.")