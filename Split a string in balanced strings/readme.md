# Split a string in balanced strings

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.


**Example 1:**

Input: s = "RLRRLLRLRL"<br>
Output: 4<br>

Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

**Example 2:**

Input: s = "RLLLLRRRLR"<br>
Output: 3<br>

Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

**Example 3:**

Input: s = "LLLLRRRR"<br>
Output: 1<br>

Explanation: s can be split into "LLLLRRRR".

**Example 4:**

Input: s = "RLRRRLLRLL"<br>
Output: 2<br>

Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
 
**Constraints:**

1 <= s.length <= 1000
s[i] = 'L' or 'R'