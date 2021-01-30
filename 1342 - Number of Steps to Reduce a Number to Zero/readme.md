# Number of Steps to reduce a Number to Zero

Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

**Example 1:**

Input: num = 14<br>
Output: 6<br>

Explanation:<br>
Step 1) 14 is even; divide by 2 and obtain 7.<br>
Step 2) 7 is odd; subtract 1 and obtain 6.<br>
Step 3) 6 is even; divide by 2 and obtain 3.<br>
Step 4) 3 is odd; subtract 1 and obtain 2.<br> 
Step 5) 2 is even; divide by 2 and obtain 1.<br> 
Step 6) 1 is odd; subtract 1 and obtain 0.<br>

**Example 2:**

Input: num = 8<br>
Output: 4<br>

Explanation:<br> 
Step 1) 8 is even; divide by 2 and obtain 4.<br> 
Step 2) 4 is even; divide by 2 and obtain 2.<br> 
Step 3) 2 is even; divide by 2 and obtain 1.<br> 
Step 4) 1 is odd; subtract 1 and obtain 0.<br>

**Example 3:**

Input: num = 123<br>
Output: 12

**Constraints:**

0 <= num <= 10^6