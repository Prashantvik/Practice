"""https://leetcode.com/problems/subarray-sum-equals-k/"""
"""==================================================="""

# Time Complexity (TC): O(n*n) | Space Complexity (SC): O(n) | TLE on leetcode
def subarraySum_brute(nums: list[int], k: int) -> int:
    count = 0

    for i in range(len(nums)):
        sum = 0
        for m in range(i, len(nums)):
            sum += nums[m]
            if sum == k:
                count += 1
    
    return count


# Time Complexity (TC): O(n*n) | Space Complexity (SC): O(n) | Use prefix logic and map | Took Help
def subarraySum_opt(nums: list[int], k: int) -> int:
    """
    The relevance of mapping sum_map[0] = 1 when k and sum matches. We should have element i.e., sum - k in the map to do count++.
    prefix_sum - k: This expression calculates the potential starting point of a subarray whose sum is equal to k. 
    If prefix_sum - k is present in sum_map, it means there is a previous
    prefix sum such that subtracting it from the current prefix_sum results in the target sum k.

    """
    count = 0
    prefix_sum = 0
    sum_map = {0: 1}

    for num in nums:
        prefix_sum += num
        
        if prefix_sum - k in sum_map:
            count += sum_map[prefix_sum - k]
        
        if prefix_sum not in sum_map:
            sum_map[prefix_sum] = 1
        else:
            sum_map[prefix_sum] += 1
    
    return count



# Testing the code
nums = [1,1,1]
k = 2
# nums = [1,2,3]
# k = 3
print(subarraySum_brute(nums, k))
print(subarraySum_opt(nums, k))