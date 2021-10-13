def calculator():
    print("Welcome to tip calculator.")
    total = float(input("What was the total bill? $"))

    bad_tip = True
    while bad_tip:
        percentage = int(input("How much tip would you like to give? 10%, 12% or 15%"))
        if percentage in [10, 12, 15]:
            bad_tip = False
        else:
            pass

    tip = 1 + percentage / 100
    people = int(input("How many people split the bill?"))
    each = round(total * tip / people, 2)
    print(f"Each person should pay {each}")


if __name__ == '__main__':
    calculator()
