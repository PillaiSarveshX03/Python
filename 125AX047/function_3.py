def choice_op():
    print('''
    PRESS 1 TO INSERT 
    PRESS 2 TO SHOW RESULT

    ''')

def choice_dis():
    print("Press 1 for SUM")
    print("Press 2 for SUBTRACTION")
    print("Press 3 for MULTIPLICATION")
    print("Press 4 for DIVISION")
    print("Press 5 TO EXIT")
    print()

def num_inp():
    n=int(input("Enter The No. of numbers : "))
    arr=[]
    for i in range(0,n):
        arr.append(int(input("Enter number:")))
    print()
    return arr



def sum ():
    result=0

    choice=1

    while choice!=2:
        choice_op()
        choice=int(input())
        if choice==1:
            result+=int(input("Enter the number :"))

    print("RESULT = ",result)

def dif ():
    result=0

    choice=1

    while choice!=2:
        choice_op()
        choice=int(input())
        if choice==1:
            result-=int(input("Enter the number :"))

    print("RESULT = ",result)

def mul ():
    result=1

    choice=1

    while choice!=2:
        choice_op()
        choice=int(input())
        if choice==1:
            result*=int(input("Enter the number :"))

    print("RESULT = ",result)

def div ():
    result=1

    choice=1

    while choice!=2:
        choice_op()
        choice=int(input())
        if choice==1:
            result/=int(input("Enter the number :"))

    print("RESULT = ",result)




print("CALCULATOR \n")

inp =1


while inp!=5:

    print()

    choice_dis()
    inp =int(input())

    if inp==5:
        break



    match inp:
        case 1: 
            print("SUM")
            sum()

        case 2: 
            print("DIFFERENECE")
            dif()

        case 3: 
            print("MULTIPLY")
            mul()
        
        case 4: 
            print("DIVISION")
            div()

        case _: print("INVALID CHOICE")


print("EXITING....")