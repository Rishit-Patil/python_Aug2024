#Accept a number as input say X and define logic to get the output say Y. The input can only be 0 or  and the output must be 1 if input is 0 and viceversa.
x=int(input("Enter the Value Of X as Either 1 or 0: "))
if x==0 or x==1:
    y=1-x
    print("Input number: ",x,"Output Number",y)
else:
    print("Invalid Input")