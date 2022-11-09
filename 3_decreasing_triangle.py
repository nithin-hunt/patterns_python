"""
* * * * *
* * * *
* * *
* *
*
"""
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
print("-----------------")

"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()
print("-----------------")

"""
ABCDE
ABCD
ABC
AB
A
"""
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end="")
    print()
