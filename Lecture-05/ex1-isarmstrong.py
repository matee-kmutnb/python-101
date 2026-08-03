def is_armstrong(number):
    # """
    # Check if a number is an Armstrong number.
    # An Armstrong number is a number that equals the sum of its own digits 
    # each raised to the power of the number of digits.
    
    # Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 ✓
    # """
    # Convert number to string to get the number of digits
    digits_str = str(number)
    num_digits = len(digits_str)
    
    # Calculate sum of each digit raised to power of number of digits
    total = 0
    for digit_char in digits_str:
        digit = int(digit_char)
        total += digit ** num_digits
    
    # Return True if total equals original number, False otherwise
    return total == number
print(is_armstrong(153))     
print(is_armstrong(370))      
print(is_armstrong(9474))     
print(is_armstrong(100))  