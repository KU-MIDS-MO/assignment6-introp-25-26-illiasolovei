##task1

# Write a function: `estimate_pi(num_samples)` that:
# returns an estimate of π using num_samples random points generated with np.random.rand().

# Idea:
# Consider: quarter of a circle of x^2+y^2=1 within a the unit square (0,0) - (1,1).
# We want to generate as much points within the unit range as the precision in tests allows us.
# Estimation of pi can then be derived from the ratio of points inside x^2+y^2=1 to their total amount.
# And since calculated for the quarter only - * 4
# Implementation follows:

import numpy as np


def estimate_pi(num_samples):
    xy = np.random.rand(num_samples, 2)
    x = xy[:, 0]
    y = xy[:, 1]

    inside = xy[(x * x) + (y * y) <= 1]
    quarter_circle_estimate = len(inside) / len(x)
    return quarter_circle_estimate * 4.0
