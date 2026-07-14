'''whenever there is a change from a letter to a digit or from a digit to a letter, his kid marks that character. By default, the first character of the string is always marked.
You have to create a new string using only the marked characters such that:
All English letters appear first.
All digits appear after the letters.
The relative order of the marked letters and marked digits should remain the same.
Return the final string.
Input Specification
input1: A string S representing an alphanumeric string.
Output Specification
Return a string formed according to the above logic.
EXAMPLE :- 
Input :-  
ABC120PME0000LZ3MB1Y3C45 
Output:- 
APLMYC103134
--------------------------------------------------
'''
s=input()
letter=""
digit=""
marked=s[0]
for i in range(1,len(s)):
    if ((s[i].isalpha() and s[i-1].isdigit()) or (s[i].isdigit() and s[i-1].isalpha())):
        if s[i].isdigit():
            digit+=s[i]
        else:
            letter+=s[i]
marked+=letter+digit
print(marked)
