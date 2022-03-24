#grading system
score1=int(input("Enter English marks"))
score2=int(input("Enter Kiswahili marks"))
score3=int(input("Enter CRE marks"))
tot=score1+score2+score3
avg=tot/5
if(avg>=90):
    print("A")
elif(avg>=80 and avg<=89):
    print("B")
elif(avg>=70 and avg<=79):
    print("C")
elif(avg>=60 and avg<=69):
    print("D")
elif(avg>=50 and avg<=59):
    print("E")
else:
    print("marks error")