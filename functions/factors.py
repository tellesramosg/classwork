from typing import List

def get_factors(num: int, prime:bool=False) -> List[int]:
    """
    Returns a list of factors for the provided num
    
    Args:
        num (int): The number for which we want factors
        
    Return:
        List[int]: A list of factors for the num
    """
    factors = []
    for i in range(1,num+1): # range returns ints numbers between start (defaults at 0), end (exclusive)
        if num % i == 0:
            factors.append(i)
    if prime:
        factors = [
            f for f in factors if len(get_factors(f) == 2)
            ]
    return factors

def get_prime_factors(num: int) -> List[int]:
    primes = []
    for i in get_factors(num):
        factors = get_factors(i)
        if len(factors) == 2:
            primes.append(i)
    return primes