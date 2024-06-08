print("         CALCULATOR           ")
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
c=int(input("enter choice(1-4):"))
if(c==1):
 print("a+b=",a+b)
elif(c==2):
 print("a-b=",a-b)

elif(c==3):
 print("a*b=",a*b)

elif(c==4):
 print("a/b=",a/b)

else:
 print("Invalid Function")
