def main():
    x, y, z = input("Expression: ").split(" ")
    print(calculator(x, y, z))

def calculator(x, y, z):
    if y == "+":
        return int(x) + int(z)
    elif y == "-":
        return int(x) - int(z)
    elif y == "*":
        return int(x) * int(z)
    elif y == "/" and int(z) != 0:
        return int(x) / int(z)
    else:
        return "Invalid operator"


main()