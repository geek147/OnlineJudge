words = input()
if(len(words)>0 and len(words)<101):
    result = []

    for ch in words:
        if str(ch).islower():
            result.append(str(ch).upper())
        elif str(ch).isupper():
            result.append(str(ch).lower())
    print(''.join(result))
