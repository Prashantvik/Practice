"""https://leetcode.com/problems/two-sum/description/"""
"""=================================================="""

# Time Complexity (TC): O(n*n) - Nested loop | Space Complexity (SC): O(1)
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for k in range(i+1, len(nums)):
            if nums[i] + nums[k] == target:
                return [i, k]



# Time Complexity (TC): O(n) | Space Complexity (SC): O(n)
def twoSum_opt(nums: list[int], target: int) -> list[int]:
    map = {}
    
    for i in range(len(nums)):
        if map and nums[i] in map:
            return [i, map[nums[i]]]
        
        map[target-nums[i]] = i


# Testing the code 
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
print(twoSum_opt(nums, target))
