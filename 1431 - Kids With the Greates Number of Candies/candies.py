def kids_with_candies(candies, extra):
    m = max(candies)
    return [c + extra >= m for c in candies]