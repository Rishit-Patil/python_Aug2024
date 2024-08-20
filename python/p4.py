#Program to accept three distinct numbers ad find smallest among them 
input_num1 = int(input("Enter the value of First Number: "))
input_num2 = int(input("Enter the value of Second Number: "))
input_num3 = int(input("Enter the value of Third Number: "))

if(input_num1 == input_num2 or input_num2 == input_num3 or input_num1 == input_num3):
    print("Two Numbers are Equal Please Enter Distinct Numbers")
else:
    if(input_num1<input_num2 and input_num1<input_num3):
        print(input_num1,"is the Smallest Number")
    elif(input_num2<input_num3 ):
        print(input_num2,"is the Smallest Number")
    else:
        print(input_num3,"is the Smallest Number")
        