from collections import Counter

s = "successes"
unli = ''
undosh = ''

for i in s:
    if i in 'aioue':
        unli += i
    else:
        undosh += i

a = max(Counter(unli).values(), default=0)
b = max(Counter(undosh).values(), default=0)

print(a + b)