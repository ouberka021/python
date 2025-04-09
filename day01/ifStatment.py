# single if

"""
if condition :
    Statements
"""
browser_name = "firefox"
if browser_name == "chrome":
    print("chrome is selected")
    print("Opening chrome Browser....")
elif browser_name == "firefox":
    print("firefox is selected")
    print("Opening firefox Browser....")
else:
    print("safari is selected")
    print("Opening safari Browser....")

    print("-----------------------------------------------")

    score = -200
    if 0 <= score <= 100:
        if score >= 60:
            print("Pass the exam")
        else:
            print("failed exam")
    else:
        print("Failed the Exam")
