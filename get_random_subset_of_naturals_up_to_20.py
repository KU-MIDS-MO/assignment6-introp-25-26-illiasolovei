##task2

# Write a function: `get_random_subset_of_naturals_up_to_20()` that:
# outputs a random subset of the set of integers between $1$ and $20$ in the format of a `numpy` array.
# The draw of the subset should be uniform, i.e., any subset should in principle have the same chance to be outputted by your function.
# This problem will be graded manually.
# For $2$ out of the $5$ points allotted to this problem, you can write your function however you wish.
# To get $5$ points, your function is allowed to make a single call to the `numpy.random.randint()` method
# but it cannot make use of any other random methods.
# ALSO: the binary representation of the numbers should be used

import numpy as np
from numpy import array


def get_bits(n, card_N):
    return "".join(str((n >> (card_N - 1 - i)) % 2) for i in range(card_N))


def get_random_subset_of_naturals_up_to_20():
    card_N = 20
    x = np.random.randint(0, 2**card_N)
    return array([i + 1 for i, b in enumerate(get_bits(x, card_N)) if b == "1"])
