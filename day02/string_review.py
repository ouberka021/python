n = "Automation Testing"
print(n[0])
print(n[-1])
#print(n[len(n)-1])

print(len(n))
# to lower case
n = n.lower()
print(n)

print("--------------------------------------------")
s= "Python Programming Language"
s1 = s[7:]
print(s1) #Programming Language

s2 = s[0:18]
print(s2) #Programming Language
#slice from the left to right I give double ::

reversed_str= s[::-1]
print(reversed_str)

reversed_str2 =''.join(reversed(s))
print(reversed_str2)
print("--------------------  String Methods ------------------------")
expected_title = "my page"
actual_title = "MY PAGE"
print(actual_title.lower() == expected_title.lower())

# LOWER
# Title
# rindex
# Upper  .....
