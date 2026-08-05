def options():
    print("""
1. Add Name
2. View Students
3. Exit
    """)


print("------------ Student System ------------")

choice=1
fname="studentdet.txt"
while(choice!=3):

    options()
    choice = int(input("Enter Your Choice : "))

    if(choice==3):
        print("Exiting......")
        break

    match(choice):
        case 1: 
                print("ADD STUDENT \n")
                with open(fname,"a") as file:
                    file.write(input("Enter Name : ")+" | ")
                    file.write(input("Enter Rno : ")+" | ")
                    file.write(input("Enter Marks : ")+" | \n")
                    print("Append Successful !!\n\n")

        case 2: 
                print("VIEW STUDENT \n")
                with open(fname,"r") as file:
                    print(file.read())
                    print("\n\n")

        case _:
                print("Incorect Option !!\n\n")
              
            


        
            
    