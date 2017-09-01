import sys

def simpleArraySum(n, ar):
    # Complete this function
    count = 0
    for i in ar:
        count = count + i
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)