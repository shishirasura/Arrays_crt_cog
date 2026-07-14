'''Input
N = 3
A = [6, 8, 1]
S = "ABC"

Output
3
'''
n=int(input())
lst=list(map(int,input().split()))
s=input()
count=0
for ch in s:
   num= ord(ch)
   while(num>0):
       rem=num%10
       if rem in lst:
           count+=1
           break
       num=num//10
print(count)
