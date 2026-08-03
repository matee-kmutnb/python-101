def generate_primes(number):
    """
    Generate a list of prime numbers up to a given number.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Example: For number = 10, the prime numbers are [2, 3, 5, 7].
    """
    primes = []
    
    for num in range(2, number + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    return primes
print(generate_primes(10))
print(generate_primes(20))
print(generate_primes(1))
print(generate_primes(2))