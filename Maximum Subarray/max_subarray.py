def max_subarray(nums):
    dp = [0]*len(nums)
    for i,num in enumerate(nums): 
        print(dp)        
        dp[i] = max(dp[i-1] + num, num)
    return max(dp)
