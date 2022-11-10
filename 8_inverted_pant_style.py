n=5
"""
1                 1 
1 2             2 1 
1 2 3         3 2 1 
1 2 3 4     4 3 2 1 
1 2 3 4 5 5 4 3 2 1 
"""
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        p-=1
        print(p,end=" ")
    print()