# Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

**Example 1:**

Input: nums = [1,2,3,4,5,6,7], k = 3<br>
Output: [5,6,7,1,2,3,4]<br>

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]<br>
rotate 2 steps to the right: [6,7,1,2,3,4,5]<br>
rotate 3 steps to the right: [5,6,7,1,2,3,4]<br>

**Example 2:**

Input: nums = [-1,-100,3,99], k = 2<br>
Output: [3,99,-1,-100]<br>

Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]<br>
rotate 2 steps to the right: [3,99,-1,-100]<br>
 

Constraints:

1 <= nums.length <= 2 * 104<br>
-231 <= nums[i] <= 231 - 1<br>
0 <= k <= 105<br>
