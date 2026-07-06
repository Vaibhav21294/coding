"""
This is one of the most common interview problems 
because it teaches how to track the minimum value seen so far while scanning an array.

Problem Statement

You are given an array prices, where:

prices[i] is the price of a stock on day i.

You want to:

Buy one stock.
Sell one stock later.
Maximize your profit.

Return the maximum profit.

If no profit is possible, return 0.

Example 1
Input:
prices = [7, 1, 5, 3, 6, 4]

Output:
5

Explanation:

Buy at 1
Sell at 6

Profit = 6 - 1 = 5

Example 2
Input:
prices = [7, 6, 4, 3, 1]

Output:
0

Explanation:

The price keeps decreasing, so there is no profitable transaction.

Brute Force Solution

Compare every possible buy day with every possible sell day.
"""

def max_profit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit

"""
Time Complexity

Two nested loops:

O(n²)
Space Complexity
O(1)
"""

def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for value in prices:
        min_price = min(value, prices[i])
        profit = value - min_price
        max_profit = max(max_profit, profit)
    return max_profit