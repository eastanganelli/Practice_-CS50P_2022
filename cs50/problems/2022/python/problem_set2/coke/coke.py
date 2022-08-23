def main():
    amount: int = 50

    while(amount > 0):
        print("Amount Due:", amount)
        v_: int = int(input("Insert Coin: "))

        amount -= v_
    
    print("Change Owed:", abs(amount))


if __name__ == "__main__":
    main()