#Below function is used to extract the numbers from the input text
def extract_numbers_from_text(text):
    l = []
    for t in text.split(" "):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

#Below functions are solving basic mathematical problems and can be extended as per requirement.
def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def end():
    print("Thanks for using me, Bye")


def sorry():
    print("This task is beyond my ability, Please code me more")

#Dict used to match the relevant keywords from the input text
operations = {"PLUS": add, "ADD": add, "ADDITION": add, "SUM": add, "+": add, "MINUS": sub, "SUB": sub, "SUBTRACT": sub, "-": sub, "MULTIPLY": mul, "*": mul, "MULTIPLICATION": mul, "DIVIDE": div, "/": div, "DIVISION": div, "BY":div}
commands = {"END": end, "EXIT": end, "CLOSE": end}
