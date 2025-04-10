# is array in java
browser = ("chrome", "Safari", "Firefox")
print(browser)

print(type(browser))
print(len(browser)) # size of turple

print(browser[1])
print(browser[-2])
a1 = browser[1:-1]
print(a1)

a2 = browser[2:]
print(a2)
a3 = browser[:-2]
print(a3)

reversed_tuple = browser[::-1]
print(reversed_tuple)

result = tuple(reversed(browser))
print(result)

print("---------------- update the element of tuple")

group_scores = ((70,30,90),(4,66,88),(7,38,9))
for i in group_scores:
    print(i)
    for j in i :
        print(j)
print("----------------")

t1 = (1,2,3,4,5)
t2 = (31,32,33,34,53)
marge_tuple = t1 + t2
print(marge_tuple)

