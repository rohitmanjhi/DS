def buyAndSellStocks(prices):
    if len(prices) == 0 and len(prices) == 1 and prices is None:
        return 0
    l,r,maxP = 0,1,0
    while r < len(prices):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r +=1
    return maxP            
prices = [7,1,5,3,6,4]
print(buyAndSellStocks(prices))
