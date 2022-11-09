"""
* 
* * 
* * * 
* * * * 
* * * * *
"""
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("-----------------")

"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
print("-----------------")

"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
print("-----------------")

"""
A 
A B 
A B C 
A B C D 
A B C D E 
"""
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
print("-----------------")

"""
A
BB
CCC
DDDD
EEEEE
"""
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end="")
    print()
print("-----------------")

"""
E
DE
CDE
BCDE
ABCDE
"""
for i in range(n):
    for j in range(i,-1,-1):
        print(chr(65+n-1-j),end="")
    print()
print("-----------------")

"""
E
ED
EDC
EDCB
EDCBA
"""
for i in range(n):
    for j in range(i+1):
        print(chr(65+n-1-j),end="")
    print()
