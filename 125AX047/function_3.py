
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



def sum (num)-> int:
    result=0 
    for n in num:
        result+=n
    return result

def dif (num)-> int:
    result=0
    for n in num:
        result-=n
    return result

def mul (num)-> int:
    result=1
    for n in num:
        result*=n
    return result

def div (num)-> int:
    result=1
    for n in num:
        result/=n
    return result




print("CALCULATOR \n")

inp =1


while inp!=5:

    print()

    choice_dis()
    inp =int(input())

    if inp==5:
        break


    
    int=num_inp()



    match inp:
        case 1: print("SUM")
                

        case 2: print("DIFFERENECE")
                

        case 3: print("MULTIPLY")
                
        
        case 4: print("DIVISION")
                

        case _: print("INVALID CHOICE")


print("EXITING....")