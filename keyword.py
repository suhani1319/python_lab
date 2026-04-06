def simple_interest(p:float,t:float,r:float):
    si=(p*t*r)/100
    print("Simple Interest:", si)

simple_interest(p=10000,t=3.4,r=2.2)

 #==> for **
n=int(input("enter numbers of line:"))   
for i in range(1,n+1):
    print("*" * i)

for i in range (1,4):
    print("*" * i)

# ==> for numbers 1 2 3 .....
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end= " ")
    print()

n=int(input("enter number of lines:"))
i=1
while i<=n:
    print("*" * i)
    i+=1

n=int(input("enter number of lines:"))
i=n
while i>=n:
    print("*" * i)
    i-=1