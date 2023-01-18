user_input = ""
cost = 0

while True:
    print("Menu: ")
    print("1. Pizza ($30)")
    print("2. Burger ($10)")
    print("3. Steak ($40)")
    print("4. Complete Order")
    
    user_input = input("Enter order: ")
    
    if user_input == "1":
        cost += 30
    elif user_input == "2":
        cost += 10
    elif user_input == "3":
        cost += 40
    elif user_input == "4":
        print("Bill: ", cost)
        break
    print("")
