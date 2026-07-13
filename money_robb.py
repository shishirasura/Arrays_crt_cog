'''You are given two integer arrays of the same size N, representing the security level and money present in houses in a city.
S[i] represents the security level of the i-th house.
M[i] represents the amount of money kept in the i-th house.
A thief wants to rob houses in the city. However, he can rob only those houses whose security level is strictly less than the average security level of all houses.
Your task is to find and return the maximum amount of money the thief can steal.
Example
Input :- 
N = 6
S = [2, 5, 3, 8, 1, 7]
M = [100, 250, 180, 500, 300, 400]
Output :- 
300
'''
//CODE
def newstring(s):
    letter=''
    digit=''
    if(s[0].isdigit()):
        digit+=s[0]
    elif(s[0].isalpha()):
        letter+=s[0]
    for ind in range(1,len(s)):
        if((s[ind-1].isdigit() and s[ind].isalpha()) or (s[ind-1].isalpha() and s[ind].isdigit())):
            if(s[ind].isdigit()):
                digit+=s[ind]
            else:
                letter+=s[ind]
    return letter+digit
s=input()
print(newstring(s))
