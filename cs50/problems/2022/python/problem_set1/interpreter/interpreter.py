def main():
    x, y, z = input("Expression: ").split(" ")
    calculator(x, y, z)

def calculator(x, y, z):
    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/" and float(z) != 0:
        print(float(x) / float(z))

main()