""" 
Find the largest palindrome made from the product of two 3-digit numbers. 

A Solution to Project Euler Question 4. 
"""

def largest_palindrome_product():
    """ 
    Calculates the largest palindromic number made from the product of two 3-digit numbers.
    Iterates through all products of two 3-digit numbers efficiently.
    Checks if the product is a palindrome by converting it to a string and comparing it to its reverse.

    Returns:
    int: The largest palindromic number found.
    """

    largest_palindrome = 0

    for i in range(999, 99, -1):
        for j in range(i, 99, -1): # Start j from i to avoid duplicate calculations
            product = i * j

            if product <= largest_palindrome:
                break

            product_str = str(product)
            if product_str == product_str[::-1]: # Reverses the string to check for palindromes

                if product > largest_palindrome:
                    largest_palindrome = product

    return largest_palindrome

result = largest_palindrome_product()
print(f"The largest palindrome made from the product of two 3-digit numbers is: {result}")