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
        print(f'Old profit: {profit}')
        print(f'list element: {prices[i]}')
        print(f'buy stock: {buy_stock}')
        profit = max(prices[i] - buy_stock, profit) # return largest argument (either prices[i] - buy_stock or old profit)
        print(f'new profit: {profit}')

    return profit