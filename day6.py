count = int(input())
lst= []
for i in range(0,count):
    lst.append(str(input()))
    
for word in lst:
    odd=[]
    even=[]
    for c in range(0,len(word)):
        if c % 2 == 0:
            even.append(word[c])
        else :
            odd.append(word[c])
    print("".join(even) + " " + "".join(odd))