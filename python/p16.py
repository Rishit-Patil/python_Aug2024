#Program to Reverse a Number
sample_number = int(input("Enter a number: "))
old=sample_number
rev_num = 0
while sample_number>0:
    temp = sample_number%10
    rev_num = (rev_num*10)+temp
    sample_number=sample_number//10
print("Reverse of a given",old,"is:",int(rev_num))