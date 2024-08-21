#Program to find the Second Smallest Digit a Number
sample_number = input("Enter a number: ")
string=[]
for i in str(sample_number):
    if i not in string:
        string.append(i)

assending_str = sorted(string)

print('The second smallest digit is: ',assending_str[1])