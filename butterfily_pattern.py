n=4
for row in range(n):
    if row<n-1:
        for col in range(row+1):
            print("*",end="")
        for col in range(2*n-2*(row+1)-1):
            print(" ",end="")
        for col in range(row+1):
            print("*",end="")
        print()
    elif row==n-1:
        for col in range(2*n-1):
            print("*",end="")
        print()
for row in range(n-1):
    for col in range(n-(row+1)):
        print("*",end="")
    for col in range((2*row)+1):
        print(" ",end="")
    for col in range(n-(row+1)):
        print("*",end="")
    print()

  
