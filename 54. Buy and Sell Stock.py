def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(max_profit, price-min_price)
        
    return max_profit

# Example Output
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5