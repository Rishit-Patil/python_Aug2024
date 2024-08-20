# Accept average score from the student of his exam and print his result as follows:  0 to 49 is Fail , 50 to 74 is Second Class , 75 to 90 is First Class, 91 to 100 is Distinction, Also check for the Invalid Score
avg_score = int(input("Enter your Average Marks: "))
if(avg_score>90 and avg_score<=100):
    print("Class: Distinction")
elif(avg_score>74 and avg_score<=90):
    print("Class: First Class")
elif(avg_score>49 and avg_score<=74):
    print("Class: Second Class")
elif(avg_score>0 and avg_score<=49):
    print("Class: Third Class")
else:
    print("Please Input Valid Average Score")