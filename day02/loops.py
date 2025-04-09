"""

in java
for(int i=0; i<5; i++){
}

"""

for i in range(0,5):
    print("for loops")

for i in range(0, 5):
        print("for loops")


print("------------ string---------------")

str = "selenium"
for x in str:
    print(x)


print("------------ ---------------")
for i in str[::-1]:
    print(i)

# reverse string
reverse_str = ""
for i in str[::-1]:
    reverse_str += i
print(reverse_str)

print("------------ Nested loop ---------------")

for i in range(0, 5):
    for j in range(1, 6):
        print("Hello selenium")

print("------------ while loop ---------------")

while True :
    print("while loop python----")
    break

score = int(input("Enter your score:\n"))
print(type(score))

while score> 100 or score < 0:
    score = int(input("Please re-enter your score:\n"))






















