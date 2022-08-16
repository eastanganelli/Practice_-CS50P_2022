input_ = input("What is the Answer ot the Great Question of Life, the Universe, and Everything? ")

string = input_.lower().replace(" ", "").replace("-", "")

match(string):
    case "42" | "forty two" | "fortytwo":
        print("Yes")
    case _:
        print("No")