def max_subarray(nums):
    dp = [0]*len(nums)
    for i,num in enumerate(nums): 
        print(dp)        
        dp[i] = max(dp[i-1] + num, num)
    return max(dp)

max_subarray([-2,1,-3,4,-1,2,1,-5,4])