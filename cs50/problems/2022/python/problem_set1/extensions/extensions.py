def main():
    mime_ = input("File name: ").lower().strip()

    if mime_.endswith(".png"):
        print("image/png")
    elif mime_.endswith(".jpeg") or mime_.endswith(".jpg"):
        print("image/jpeg")
    elif mime_.endswith(".gif"):
        print("image/gif")
    elif mime_.endswith(".txt"):
        print("text/plain")
    elif mime_.endswith(".pdf"):
        print("application/pdf")
    elif mime_.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()