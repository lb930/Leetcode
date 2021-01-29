# Best time to buy and sell stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**

Input: [7,1,5,3,6,4]<br>
Output: 5<br>
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.<br>
Not 7-1 = 6, as selling price needs to be larger than buying price.

**Example 2:**

Input: [7,6,4,3,1]<br>
Output: 0<br>
Explanation: In this case, no transaction is done, i.e. max profit = 0.

# Best time to buy and sell stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

**Example 1:**

Input: [7,1,5,3,6,4]<br>
Output: 7<br>

Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

**Example 2:**

Input: [1,2,3,4,5]<br>
Output: 4<br>

Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

**Example 3:**

Input: [7,6,4,3,1]<br>
Output: 0<br>

Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

**Constraints:**

1 <= prices.length <= 3 * 10 ^ 4<br>
0 <= prices[i] <= 10 ^ 4<br>