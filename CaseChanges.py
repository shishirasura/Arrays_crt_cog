'''You are given a string S consisting only of uppercase and lowercase English letters.
You have to count how many times the case changes between consecutive characters in the string.
A case change occurs when:
a lowercase letter is followed by an uppercase letter, or
an uppercase letter is followed by a lowercase letter.
Your task is to find and return an integer representing the number of case changes in the string.
Input
aBcD
Output
3
Explanation
The string is "aBcD".
Compare every pair of consecutive characters:
a → B (lowercase → uppercase) ✅ Case changed
B → c (uppercase → lowercase) ✅ Case changed
c → D (lowercase → uppercase) ✅ Case changed
Total case changes = 3
Hence, the output is:
3
'''
//CODE
s=input()
count=0
for i in range(0,len(s)-1):
    if ((s[i].isupper() and s[i+1].islower()) or (s[i].islower() and s[i+1].isupper())):
        count+=1
print(count)
