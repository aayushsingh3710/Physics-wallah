# we create username for user
name=input("Enter your Name:")
b=0
for i in name:
  b=b+1
print("@",name,b)
# tell about prime nature
a=int(input("Enter a No:"))
b=0
for i in ranfe(1,a+1):
  if a%i==0:
    b=b+1
  if b==2:
    print("It is a Prime no")
  else:
    print("It is not a Prime no")
