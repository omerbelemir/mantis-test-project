"""Statistical utility functions."""

import math
from typing import List


def mean(values: List[float]) -> float:
    """Calculate the arithmetic mean."""
    if not values:
        raise ValueError("Cannot compute mean of empty list")
    return sum(values) / len(values)


def median(values: List[float]) -> float:
    """Calculate the median value."""
    if not values:
        raise ValueError("Cannot compute median of empty list")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]


def std_dev(values: List[float]) -> float:
    """Calculate the population standard deviation."""
    if len(values) < 2:
        raise ValueError("Need at least 2 values for std_dev")
    avg = mean(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return math.sqrt(variance)
