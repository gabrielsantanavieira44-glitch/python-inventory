bag = []

while True: 
    print("\n   Your bag  \n----------------")
    print("1: • Add a item")
    print("2: • Show your bag")
    print("3: • Remove a item")
    print("0: • Exit")
    
    choose = input("Choose: ")
    
    if choose == "1":
        add = input("What item you want add? ")
        bag.append(add)

    elif choose == "2":
        print(f"This is your bag: {bag}")

    elif choose == "3":
        remove = input("Remove which item? ")
        if remove in bag:
            bag.remove(remove)
        else:
            print("item not found")

    elif choose == "0":
        print("Ok.")
        break

    else:
        print("invalid")