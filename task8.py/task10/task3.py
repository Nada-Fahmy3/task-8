customers = [("Alex", "VIP"), ("Bob", "Regular"),("Sarah", "Regular"),
    ("Maria", "VIP"), ("Mike", "Regular")]

vip = []
regular = []

for customer in customers:
    name,type = customer
    if type == "VIP":
        vip.append(name)
    else:
        regular.append(name)

serving_order = vip + regular

print(serving_order)
