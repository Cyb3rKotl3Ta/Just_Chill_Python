# Enter number of terms needednbsp;#0,1,1,2,3,5....
a=int(input("Enter the terms\n>>> "))
f=0;#first element of series
s=1#second element of series
if a==0:
   print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        print(next,end=" ")
        f=s
        s=next