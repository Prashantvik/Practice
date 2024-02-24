"""https://leetcode.com/problems/check-if-n-and-its-double-exist/description/"""
"""=========================================================================="""


# Time Complexity (TC): O(n) | Space Complexity (SC): O(n)
def checkIfExist(nums : list[int]) -> bool:
    map = {}
    for i in range(len(nums)):
        map[nums[i]] = i
        
    for i in range(len(nums)):
        if map and 2*nums[i] in map:
            if i != map[2*nums[i]]:
                return True

    return False


def checkIfExist_set(nums : list[int]) -> bool:
    num_set = set()
        
    for i, num in enumerate(nums):
        if 2 * num in num_set or (num % 2 == 0 and num // 2 in num_set):
            return True
        num_set.add(num)
    
    return False


def checkIfExist_mycore(nums : list[int]) -> bool:
    map = {}
        
    for i in range(len(nums)):
        if map:
            if 2*nums[i] in map:
                if i != map[2*nums[i]]:
                    return True

        if map and nums[i]%2 == 0:
            if nums[i]//2 in map:
                if i != map[nums[i]//2]:
                    return True

        map[nums[i]] = i

    return False


# How we have reduced the logic code line from mycore to core below
# Using vulnerable conditions before and possible failure ones
def checkIfExist_core(nums : list[int]) -> bool:
    num_dict = {}

    for i in range(len(nums)):
        if 2 * nums[i] in num_dict and i != num_dict[2 * nums[i]]:
            return True

        if nums[i] % 2 == 0 and nums[i] // 2 in num_dict and i != num_dict[nums[i] // 2]:
            return True

        num_dict[nums[i]] = i

    return False



# Testing the code 
arr = [10,2,5,3]
print(checkIfExist(arr))