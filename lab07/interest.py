def investment_value(start, interest_rate, years, tax_rate, deposit):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance


def years_to_reach_goal(start, interest_rate, tax_rate, deposit, goal):
    years = 0
    balance = start
    while balance < goal:
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
        years += 1
    return years