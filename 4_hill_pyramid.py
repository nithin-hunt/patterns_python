n=5
"""
     *
    ***
   *****
  *******
 *********
"""
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
print("-----------------")

"""
     A
    ABA
   ABCBA
  ABCDCBA
 ABCDEDCBA
"""
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print(chr(65+j),end="")
    for j in range(i-1,-1,-1):
        print(chr(65+j),end="")
    print()
    