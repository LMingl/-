""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def divide(m):
        if n == m:
            return True
        elif n % m == 0:
            return False
        else:
            return divide(m + 1)

    return True if n == 1 else divide(2)    



def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a > b:
        big, small = a, b
    else:
        big, small = b, a

    if big % small == 0:
        return small
    else:
        return gcd(small, big % small)



def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def times(quotient, m):
        sums = 0
        while quotient:
            if(quotient % 10) + m == 10:
                sums += 1
            quotient = quotient // 10
        return sums

    return 0 if n // 10 == 0 else ten_pairs(n // 10) + times(n // 10, n % 10)
    
    
