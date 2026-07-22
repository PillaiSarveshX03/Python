
def choice_dis():
    print("Press 1 for SUM")
    print("Press 2 for SUBTRACTION")
    print("Press 3 for MULTIPLICATION")
    print("Press 4 for DIVISION")
    print("Press 5 TO EXIT")
    print()




def sum (a,b)-> int: 
    return a+b

def dif (a,b)-> int:
    return a-b

def mul (a,b)-> int:
    return a*b

def div (a,b)-> int:
    return a/b





print("CALCULATOR \n")

inp =1


while inp!=5:

    print()

    choice_dis()
    inp =int(input())

    if inp==5:
        break


    a =int(input("Enter A :"))
    b =int(input("Enter B :"))



    match inp:
        case 1: print("SUM :" , sum(a,b))

        case 2: print("DIFFERENECE :" , dif(a,b))

        case 3: print("MULTIPLY :" , mul(a,b))
        
        case 4: print("DIVISION :" , div(a,b))

        case _: print("INVALID CHOICE")


print("EXITING....")