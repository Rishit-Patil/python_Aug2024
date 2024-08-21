#Program to Find Sum of Digits of a Number
number=int(input("Enter a Number to Find the Sum of its Digits: "))
k=0
add=0
old=number
while(number>0):
    k=number%10
    add+=k
    number=number/10
print("The Sum of Digits of ",old," is :",int(add))
    


