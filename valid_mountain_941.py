"""https://leetcode.com/problems/valid-mountain-array/description/"""
"""==============================================================="""


# Time Complexity (TC): O(n) | Space Complexity (SC): O(1)
def validMountainArray(nums: list[int]) -> bool:
    numslen = len(nums)
    start = 0
    end = numslen - 1

    # Ascend to the peak
    while start < numslen - 1 and nums[start] < nums[start + 1]:
        start += 1

    # Descend from the peak
    while end > 0 and nums[end] < nums[end - 1]:
        end -= 1

    # Check if the peak is not at the beginning or end
    return 0 < start < numslen - 1 and start == end



# How code can be simplified to understand the logic better | Good coding practice
def validMountainArray_simplified(nums : list[int]) -> bool:
    numslen = len(nums)
        
    if numslen < 3:
        return False

    start = 0

    # Ascend to the peak
    while start < numslen - 1 and nums[start] < nums[start + 1]:
        start += 1

    # Check if peak is not at the beginning or end
    if start == 0 or start == numslen - 1:
        return False

    # Descend from the peak
    while start < numslen - 1 and nums[start] > nums[start + 1]:
        start += 1

    return start == numslen - 1



# Testing the code 
arr = [0,3,2,1]
print(validMountainArray(arr))
print(validMountainArray_simplified(arr))