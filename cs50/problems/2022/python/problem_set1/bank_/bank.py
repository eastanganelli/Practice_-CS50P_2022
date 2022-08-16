input_ = input("Greeting: ")

pos = input_.lower().find("h")

if input_.lower().find("hello") == 0:
    print("$0")
elif input_.lower().find("h") == 0:
    print("$20")
else:
    print("$100")