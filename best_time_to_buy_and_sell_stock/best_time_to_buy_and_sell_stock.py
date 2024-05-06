"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


def maxProfit(prices: list[int]) -> int:
    max_profit:int = 0
    min_value:int = prices[0]
    max_value:int = 0
    for price in prices[1:]:
        if price < min_value:
            min_value = price
            max_value = 0
        elif price > min_value and price >= max_value:
            max_value = price
            if max_profit < max_value -min_value:
                max_profit = max_value-min_value
    return max_profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([2,1,2,1,0,1,2]))
print(maxProfit([3,3,5,0,0,3,1,4]))
print(maxProfit([3,2,6,5,0,3]))
