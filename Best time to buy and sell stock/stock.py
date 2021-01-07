from itertools import combinations

def stock(prices):
    
    if not prices:
        return 0

    profit = 0
    buy_stock = prices[0]

    for i in range(len(prices)):

        # update the buy_stock if there's any smaller value present in the list
        if buy_stock > prices[i]:
            buy_stock = prices[i]

        # Calculate the max of price diff and profit made until now
        profit = max(prices[i] - buy_stock, profit)

    return profit
