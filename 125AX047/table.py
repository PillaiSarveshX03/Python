print("Welcome to the Multiplication Table Generator!")

choice =1

print("PRESS 1 FOR MULTIPLICATION TABLE")
print("PRESS 2 TO STOP")
choice =int(input())

while choice == 1:
    n =int(input("Enter a number: "))

    print(f"Multiplication Table for {n}:")

    print()
    m = 1

    for i in range(0, 10):
        print(f"{n} X {m} = {n*m}")
        m += 1
        
    print()
    print()

    print("PRESS 1 FOR MULTIPLICATION TABLE")
    print("PRESS 2 TO STOP")
    choice =int(input())

print()
print("EXITING THE PROGRAM....")

