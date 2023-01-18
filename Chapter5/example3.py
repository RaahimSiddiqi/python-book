

def calculate_bill(price, membership):
    if membership == "Regular":
        print(price * 1.0)
    elif membership == "Silver":
        print(price * 0.9)
    elif membership == "Gold":
        print(price * 0.75)
    else:
        print("Membership type was invalid")
    
price = 1000
membership_type = "Silver"
calculate_bill(price, membership_type)