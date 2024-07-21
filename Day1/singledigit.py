def sum_of_digits_until_single_digit(number):
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))
    
    while number >= 10:
        number = sum_of_digits(number)
    
    return number

number = 23456
result = sum_of_digits_until_single_digit(number)
print(f"The single digit sum is: {result}")