def main():
    salutate = input("Greeting: ")

    salutate = salutate.lower()

    if salutate.startswith("hello"):
        print("$0")
    elif salutate.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()