for i in range (5):
    print(i)
for i in range (3,5):
    print(i)
    
#print 2 table using loop
for i in range (1,11):
      print(i,"x2=",i*2)

#get input for a number.print number between a and b (sample input=8,15)
for i in range (8+1,15):
    print (i)

#print even number between 1 to 10
for i in range (1,10):
 if (i%2==0):
    print(i)

#count the number of even numbers between 1 to 10
count=0
for i in range (1,11):
     if(i%2==0):
         count=count+1
print(count)

#count the number of odd and even numbers between 1 to 10 and print it.
e_count=0
o_count=0
for i in range(1,11):
  if(i%2==0):
      e_count=e_count+1
  else:
      o_count=o_count+1
print(e_count)
print(o_count)

#count the numbers of divisible by 3 and 5
count=0
for i in range(1,101):
    if (i%3==0 and i%5==0):
        count=count+1
print(count)        
      
      
