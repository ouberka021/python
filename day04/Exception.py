from logging import exception



try:
    x = 100/0
    print(x)
except Exception:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("Finally Block")

print("test completed")

print("----------------------------")

try:
    raise  IndexError
except AttributeError:
    print("Exception is AttributeError ")
except OSError:
    print("Exception is OSError ")
except SyntaxError:
    print("Exception is SyntaxError ")
print("----------------------------")
raise  Exception("Program now is terminated")

