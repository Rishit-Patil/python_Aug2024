#Program to Find the Count of Digits of a Number
number=int(input("Enter a Number to Find the Count of Digits: "))
old=number
count=0
if (number==0):
    count=1
else:
    while number>0:
        number=number//10
        count=count+1
print("The No. of Digits in",old,"are:",count)
