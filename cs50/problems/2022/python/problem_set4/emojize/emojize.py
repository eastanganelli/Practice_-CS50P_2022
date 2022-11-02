import emoji

def main():
    input_emoji: string = input("Input: ").lower().strip()

    print(f"Output: {emoji.emojize(input_emoji, language='alias')}")

if __name__ == "__main__":
    main()