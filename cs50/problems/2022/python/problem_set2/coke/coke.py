def main():
    amount: int = 50

    while(amount > 0):
        print("Amount Due:", amount)
        v_: int = int(input("Insert Coin: "))

        if v_ == 25 or v_ == 10 or v_ == 5:
            amount -= v_
    
    print("Change Owed:", abs(amount))


if __name__ == "__main__":
    main()