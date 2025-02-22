print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
     ''')
NUM1=int(input("enter ist number:"))
NUM2=int(input("enter 2nd number:"))
opr=input("enter the operator(+,-,*,/):")
if opr=="+":
    print(NUM1+NUM2)
elif opr=="-":
    print(NUM1-NUM2)
elif opr=="*":
    print(NUM1*NUM2)
elif opr=="/":
    print(NUM1/NUM2)
else:
    print("invalid operator")