#Beginner's way.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y



print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")



while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")





# def add(x, y):
#     return x+y


# def substract(x, y):
#     return x-y


# def multiply(x, y):
#     return x*y


# def divide(x, y):
#     if  num2 == 0:
#         return "Error! Can't diivde 0."
#     return x/y

# print("Choose a number: ")
# print("1. add")
# print("2. substract")
# print("3. multiply")
# print("4. divide")

# choice = input("Choose an operation between 1 and 4: ")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if choice == "1":
#     print("Result: " + add(num1, num2))
# elif choice == "2":
#     print("Result: " + substract(num1, num2))
# elif choice == "3":
#     print("Result: " + multiply(num1, num2))
# elif choice == "4":
#     print("Result: " + divide(num1, num2))
# else:
#     print("Wrong choice number, re-enter it.")

# while True:
#     print("5. Exit")

#     choice = input("Enter choice (5): ")

#     if choice == '5':
#         print("Exiting calculator. Goodbye!")
#         break

#(The last version kills the loop, it does not loop back if you make a mistake)
































#Pro's way

# import tkinter as tk

# calculation = ""

# def add_to_calculation(symbol):
#     global calculation
#     calculation += str()


# def add_to_calculation(symbol):
#     pass


# def add_to_calculation(symbol):
#     pass

# root = tk.Tk()
# root.geometry("300x275")

# text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
# text_result.grid(columnspan=5)

# root.mainloop()


