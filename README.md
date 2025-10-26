# Largest-Palindrome-Product

A Python solution for Project Euler Problem 4: "Find the largest palindrome made from the product of two 3-digit numbers."
This was a fun, personal challenge to practise algorithmic thinking in Python.

## About the Code:
This solution is more efficient than a simple "brute-force" check. It achieves this in two ways:

1. Reduced Calculations: The inner loop (j) starts from i. This avoids calculating the same product twice (e.g., it calculates 999 * 998, but not 998 * 999), effectively halving the search time.

2. Optimised Search: Once a new largest_palindrome is found, the inner loop includes a break statement. This stops the loop from checking any further products that are guaranteed to be smaller, saving a lot of time.
