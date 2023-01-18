
price = 1000
membership_type = "Silver"
bill = 0

if membership_type == "Regular":
    bill = price * 1.0
elif membership_type == "Silver":
    bill = price * 0.9
elif membership_type == "Gold":
    bill = price * 0.75
else:
    print("Membership type was invalid")

print("Bill: ", bill)