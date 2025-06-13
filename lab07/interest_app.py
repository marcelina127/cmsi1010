import locale
from interest import investment_value, years_to_reach_goal 
locale.setlocale(locale.LC_ALL, 'en_US')

print("Welcome to the interest app!")

while True:
    option = input("What would you like to do? Enter 'value', 'goal', or 'exit':")
    option = option.strip().lower()
    match option:
        case "value":
            print (investment_value)
        case "goal":
            print (years_to_reach_goal)
        case "exit":
            break
print(investment_value(start=10000, 
                       tax_rate=.13, 
                       years=25, 
                       interest_rate=0.07, 
                       deposit=500))

print(years_to_reach_goal(start= 10000,
                         tax_rate= 0.25,
                         interest_rate=0.13,
                         deposit=1000,
                         goal= 1000000))

