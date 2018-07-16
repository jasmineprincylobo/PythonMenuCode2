def fact(n):
    f=1
    while(n>0):
        f*=n
        n-=1
    return f
loop=1





while loop == 1:
   
   
   print("1.print odd values")
   print("2.print even values")
   print("3. multiple of 3")
   print("4.fact")
   print("5.mul table of n")
   print("6.exit")
   ch=int(input("enter ur choice:"))
   if(ch<6):
    try: n=int(input("enter number:"))
   
    except ValueError:print("not a no.")
     ch=8
   
   
    if ch==1:print([x for x in range(n+1) if x%2==1])
    elif ch==2:print([x for x in range(1,n+1)if x%2==0])
    elif ch==3:print([x*3 for x in range(1,n+1)])
    elif ch==4:print(fact(n))
    elif ch==5:
              for x in range(1,11):
                print(n, '*', x ,'=', n*x)
   if ch==6:loop=0

