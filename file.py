## READ

# file = open("example.txt","r")

# print(file.read())
# print(file.readline())
# print(file.readlines())

# file.close()


## WRITE

# file = open("example.txt","w")

# file.write(input("Enter Sample Text :"))

# file.close()



## APPEND

# file = open("example.txt","a")

# file.write(input("Enter Sample Text :"))
# file.close()


with open("example.txt","r") as file:
    print(file.read(10))
