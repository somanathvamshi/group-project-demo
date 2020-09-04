import addition
import division
import modulo
import multi
import sub

print("Select operation :\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulo\n")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", addition.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub.substract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multi.multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division.divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", modulo.modulo(num1, num2))
        break
    else:
        print("Invalid Input")
