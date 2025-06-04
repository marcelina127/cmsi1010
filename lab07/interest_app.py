import locale
from interest import investment_value, years_to_reach_goal 

print("Welcome to the interest app!")

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

locale.setlocale(locale.LC_ALL, 'ru_RU')
print(locale.currency(3552.99315, grouping=True))
locale.setlocale(locale.LC_ALL, 'en_US')
print(locale.currency(3552.99315, grouping=True))
locale.setlocale(locale.LC_ALL, 'en_GB')
print(locale.currency(3552.99315, grouping=True))