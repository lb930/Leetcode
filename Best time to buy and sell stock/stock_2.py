def max_profit(prices):

    price_gain = []

    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            price_gain.append(prices[i + 1] - prices[i])
    return sum(price_gain)
