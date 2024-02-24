"""https://leetcode.com/problems/contains-duplicate/"""
"""================================================="""

# Time Complexity (TC): O(nlogn) | Space Complexity (SC): O(1)
def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
        
    return False

# Time Complexity (TC): O(n) | Space Complexity (SC): O(N)
def containsDuplicate_hash(nums: list[int]) -> bool:
    map = {}

    for num in nums:
        if num in map.keys():
            map[num] += 1
            if map[num] > 1: 
                return True
        else:
            map[num] = 1
        
    return False


# More tricky | HashSet
def containsDuplicate_set(nums: list[int]) -> bool:
    if len(nums) == len(set(nums)):
        return False
    return True

# Testing the code
nums = [1,2,3,1]
nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,4]
print(containsDuplicate(nums))
print(containsDuplicate_hash(nums))
print(containsDuplicate_set(nums))