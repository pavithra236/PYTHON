#get input for variable mark.if mark>35 print pass.else print fail.
mark=int(input())
if(mark>35):
  print("pass")
else:
  print("fail")

#get input for variable income.if income is greater than 7ooo scholarship is available .else not eligible for scholarship.
income=int(input("income"))
if(income>=7000):
    print("scholarship is available")
else:
    print("not eligible")
    
#get input for a number and check it is divisible by both 3 and 5.if yes then print the number is divisible by 3 and 5 else the number is not divisible by 3 and 5.
nmb=int(input("nmb"))
if(nmb%3==0 and nmb%5==0):
  print("the number is divisible by 3 and 5")
else:
   print("the number is not divisible by 3 and 5")

#get input for number and find it is even or odd   
b=int(input("b"))
if(b%2==0):
  print("even")
else:
   print("odd")
   
#get input for score out of 100 (1)score<35 means poor student (2)score>35 but<70 means average student (3)score>=70 means good student
score=int(input("score"))
if(score<=35):
  print("poor student")
if(score>=35 and score<70):
    print("average student")
if(score>=70):
      print("good student")

#make a mini calculator
a=int(input("a"))
b=int(input("b"))
operation=input("add/sub/mul/divi")
if(operation=="add"):
  print(a+b)
elif(operation=="sub"):
  print(a-b)
elif(operation=="mul"):
  print(a*b)
elif(operation=="divi"):
  print(a/b)
else:
  print("invalid")

scorepercentage=int(input("score percentage"))
if (scorepercentage>=70):
  name=input("enter your name")
  age=input("enter your age")
  print("your eligible")
else:
  print("your not eligible")

salary=int(input("salary"))
age=int(input("age"))
if(salary>=20000 or age<=25):
  loan=int(input("loan"))
  if(loan<=50000):
    print("your eligible for loan")
  else:
     print("maxi amount is 50000")
else:
  print("your not eligible")
      
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
d=int(input("d"))
e=int(input("e"))
f=(a+b+c+d+e)/5
if (f<35):
  print("Additional class is required")
else:
  print("you are good to go")
   
