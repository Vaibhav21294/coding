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

Optimized Solution (One Pass)

The key observation:

At any day, the best stock to buy is the lowest price seen so far.

So while scanning from left to right, keep track of:

min_price = lowest price seen so far
max_profit = best profit found so far

For each price:

Update the minimum price if today's price is lower.
Otherwise, calculate the profit if you sold today.
Update the maximum profit.

"""
def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

"""
Time Complexity

We scan the array once.

O(n)
Space Complexity

Only two variables are used:

min_price
max_profit
O(1)

Brute Force vs Optimized
| Approach    | Time     | Space    |
| ----------- | -------- | -------- |
| Brute Force | O(n²)    | O(1)     |
| One Pass    | **O(n)** | **O(1)** |

Interview Explanation (30 seconds)

If the interviewer asks, "How did you optimize it?", you can say:

"The brute-force solution compares every buy day with every later sell day, 
resulting in O(n²) time. We can optimize it by scanning the array once while maintaining the minimum stock price seen so far. 
For each day's price, we calculate the profit if we sold on that day and update the maximum profit. 
This reduces the time complexity to O(n) while using only O(1) extra space."

💡 Pattern to Remember

This problem teaches the "Track the Best Value So Far" pattern.

Whenever you're asked to maximize or minimize something while scanning an array, ask yourself:

"Can I keep track of the best value seen so far instead of recomputing it?"

You'll see this pattern again in many interview problems.
"""