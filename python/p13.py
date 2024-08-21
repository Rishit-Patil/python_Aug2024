#Program to find the biggest (smallest) digit in a number
number=int(input("Enter a Number to find the Biggest digit in it : "))  # Replace "Biggest" with "Smallest" 
list=[]
k=0
if number==0:
    print("The Only Digit Big or Small = 0")
else:
    while number>0:
        k=number%10
        list.append(k)
        number=number//10
    print(max(list)) #Use min() Function to get the Smallest Number from the List
        