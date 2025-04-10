items = ["Pen","Laptop","Book","Camera"]
print(items)
print(type(items))
print(type(items))
print(len(items))


items.append("Microphone")
print(items)
items.pop(-2)
print(items)
items.remove("Pen")
print(items)

items.extend(("Eggs","Apples","Orange"))
print(items)

print("----------------------------------")
languages = ("Jave", "Javascript", "C#", "Python", "Ruby","TypeScript")

temp_list = list(languages)
temp_list.pop(1)
temp_list.remove("Ruby")
print(temp_list)