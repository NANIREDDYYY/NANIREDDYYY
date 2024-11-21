name=input("Enter your name: ")
m=int(input("Enter your marks:"))
if(m>=90):
    print("A Grade")
elif(80<=m<=89):
    print("B grade")
elif(70<=m<=79):
    print("C grade")
elif(60<=m<=69):
    print("D grade")
else:
    print("Fail")