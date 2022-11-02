vowels: str = 'aAeEiIoOuU'

def main():
    in_: str = input("Input: ")
    out_: str = rm_vowels(in_)
    print("Output:", out_)


def rm_vowels(text: str):
    for i in range(len(vowels)):
        text = text.replace(vowels[i], "")
    
    return text



if __name__ == "__main__":
    main()