"""https://leetcode.com/problems/find-peak-element/description/"""
"""============================================================"""

# Time Complexity (TC): O(n) | Space Complexity (SC): O(1)
def findPeakElement(nums: list[int]) -> int:
    numslen = len(nums)

    if numslen == 1:
        return 0
    if numslen == 2:
        return 0 if nums[0] > nums[1] else 1 
    
    for i in range(len(nums)):
        if i == 0 and nums[i] > nums[i+1]:
            return 0
        if i == numslen-1 and nums[i-1] > nums[i-2]:
            return i
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i


# Thought of binary search but didn't know how to implement in such scneario
# Time Complexity (TC): O(logn) | Space Complexity (SC): O(1) | Binary Search
def findPeakElement_opt(nums: list[int]) -> int:
    """
    We know that for all i, nums[i] != nums[i+1] and nums[-1] == nums[n] == -INF. From these conditions, we can prove that there must 
    exist such an i that is peak, nums[i] > nums[i-1] and nums[i] > nums[i+1]:
    Suppose there is no i such that nums[i] > nums[i-1] and nums[i] > nums[i+1], then there are two cases:

    1. if nums[i] > nums[i-1], it implies nums[i] < nums[i+1] for all i. however, this contradicts nums[n] == -INF
    2. if nums[i] > nums[i+1], it implies nums[i] < nums[i-1] for all i which contradicts nums[-1] == -INF

    Now we know that there must exist a peak i, we can derive the algorithm - 
    -> if nums[m] < nums[m+1], then we know the right half is also an array where for all i, nums[i] != nums[i+1] 
    and nums[-1] == nums[n] == -INF (or to be more precise any x such that x < nums[i_0] && x < nums[i_n-1] 
    and we know there must exist a peak
    -> if nums[m] > nums[m+1], same logic applies for the left half
    """
    if len(nums) == 1:
        return 0 

    numslen = len(nums)

    # check if 0th/n-1th index is the peak element - Imp
    if nums[0] > nums[1]:
        return 0
    if nums[numslen - 1] > nums[numslen - 2]:
        return numslen - 1

    # How are we initializing the low and high
    # search in the remaining array
    low, high = 1, len(nums) - 2

    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] < nums[mid-1]:
            high = mid - 1
        elif nums[mid] < nums[mid+1]:
            low = mid + 1
        
    return -1


# Testing the code
nums = [1,2,3,1]
print(findPeakElement(nums))
print(findPeakElement_opt(nums))