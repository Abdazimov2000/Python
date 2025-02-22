def calculate_discount(price: float, discount: float=10)->float:
    x = price - (price * discount/100)
    return x
y = calculate_discount(100_000)
print(y)
