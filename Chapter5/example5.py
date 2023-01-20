

def calculate_bill(price, membership):
    if membership == "Regular":
        return price * 1.0
    elif membership == "Silver":
        return price * 0.9
    elif membership == "Gold":
        return price * 0.75
    else:
        return -1
    
print(calculate_bill(1000, "Silver"))
print(calculate_bill(5000, "Gold"))
print(calculate_bill(500, "Regular"))
print(calculate_bill(999, ""))
