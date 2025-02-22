def calculate_interest(principal: float, rate: float = 5, time: int = 1)-> float:
    x = (principal * rate * time) / 100
    print(x)
calculate_interest(50_000_000)
