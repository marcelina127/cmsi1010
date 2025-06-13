def blocks(n):
    return 0 if n<=0 else blocks(n-1) + n




def factorial(n):
    return 1 if n <=1 else (n-1) * n 

def is_palindrome(s):
    return True if s == s[::-1] else False

def sum_of_digits(n):
    return 0 if n==0 else sum_of_digits (n//10) + (n%2)

def print_count_down(n): 
    if n==0:
        print("BOOM") 
    else:
        print(n)
        print_count_down(n -1)


