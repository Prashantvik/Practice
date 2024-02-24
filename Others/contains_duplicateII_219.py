"""https://leetcode.com/problems/contains-duplicate-ii/"""
"""===================================================="""

# Time Complexity (TC): O(nlogn) | Space Complexity (SC): O(1)
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True
    
    return False


def containsNearbyDuplicate_opt(nums: list[int], k: int) -> bool:
    map_elem = {}

    for i in range(len(nums)):
        if nums[i] in map_elem.keys():
            if abs(map_elem[nums[i]] - i) <= k:
                return True
            
        map_elem[nums[i]] = i

    return False



# Testing the code
nums = [1,2,3,1]
k = 3
# nums = [1,0,1,1]
# k = 1
# nums = [1,2,3,1,2,3]
# k = 2
print(containsNearbyDuplicate(nums, k))
print(containsNearbyDuplicate_opt(nums, k))