#basic calculator program

def calculator():
    print("================================================================")
    print(" 1.Add(+)\n 2.Sub(-)\n 3.Mul(*)\n 4.Div(/)")
    x = input("Please select the operation you want to do(enter the number):")
    if x in ['1', '2', '3', '4']:
        a = int(input("Enter number1: "))
        b = int(input("Enter number2: "))

        if x == '1':
            print("%d + %d = %d"%(a,b,a+b))
        elif x == '2':
            print("%d - %d = %d"%(a,b,a-b))
        elif x == '3':
            print("%d * %d = %d"%(a,b,a*b))
        else:
            print("%d / %d = %d"%(a,b,a/b))
    else:
        print("You have entered invalid number")

    req=input("Do you wish to continue press 'Yes' else press 'No':")
    if req == 'Yes' or req == 'yes':
        calculator()
    else:
        exit()
calculator()
