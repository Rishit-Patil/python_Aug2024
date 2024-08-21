#Program to find the Second Smallest Digit a Number
number=int(input("Enter a Number to Find its Second Smallest Digit: "))
string=[]
old = number
while number>0:
    k=number%10
    string.append(k)
    number=number//10
ascending_string = sorted(string)
print("The Second Smallest Digit in",old,"is :", ascending_string[1])