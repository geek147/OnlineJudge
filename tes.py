#  Toggle String

# from hackerearth
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/

# You have been given a String S
# S consisting of uppercase and lowercase English alphabets. 
# You need to change the case of each alphabet in this String.
# That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. 
# You need to then print the resultant String to output.

words = input()
if(len(words)>0 and len(words)<101):
    result = []

    for ch in words:
        if str(ch).islower():
            result.append(str(ch).upper())
        elif str(ch).isupper():
            result.append(str(ch).lower())
    print(''.join(result))
