elememts = {0}
print(type(elememts))
print(elememts)

elememts.add(10)
elememts.add(40)
elememts.add(10)
elememts.add(60)
elememts.add(10)
elememts.add(10)
elememts.add(10)
elememts.add(10) # no duplicate value
print(elememts)
elememts.remove(10)
print(elememts)
elememts.pop() # removing 0
print("---------------------------")
# to get help from python use
print(help(set.update))

print(elememts)

print("--------------------")
s1 = {"selenium", "cypress", "playwright"}
s2 = {"selenium", "java", "UFI"}
s3 = s2.difference(s2)
print(s3)