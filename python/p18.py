#Program to Find Odd Placed Even Digits in a number 
sample_number=int(input("Enter A Number: "))
str_1=str(sample_number)
print("The Odd Placed Even Digits in the",sample_number,"are:")
for i in range (0,len(str_1),2):
    if (int(str_1[i])%2==0):
        print(str_1[i])







