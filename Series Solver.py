# #boiler plate
# import numpy as np

# #define function
# def series_sum(n):
# # Create an array of indices from 1 to n
# i = np.arange(1, n + 1)

# # Calculate the vale off each term in the series
# term = 2 / (3 ** (i - 1))

# # return sum of all terms
# return np.sum(term)

# # compute and print the first four partial sums
# for n in range(1, 5):
# print(f"S_{n} = {series_sum(n):.4f}")

import sympy as sp
# Define symbols for sympy
i, n = sp.symbols('i n')

# Define the general formula for the series
a_i = 2 / (3 ** (i - 1))

# Create ethe summation formula from i=1 to n
series_sum = sp.Sum(a_i, (i, 1, n))

# Evaluate the summation for specific values of n
for steps in range(1, 6):
    partial_sum = series_sum.subs(n, steps).doit()
    print(f"S_{steps} = {partial_sum}")
