"""https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/"""
"""==========================================================================="""

# Time Complexity (TC): O(n) | Space Complexity (SC): O(k) where k is the unique elements in nums 
def minimumOperations_map(nums: list[int]) -> int:
    seen = {}
    count = 0

    for num in nums:
        if num != 0:
            if num in seen.keys():
                pass
            else:
                seen[num] = True
                count += 1

    return count
    

# Time Complexity (TC): O(n) | Space Complexity (SC): O(n) 
def minimumOperations_lis(nums: list[int]) -> int:
    """
    For every smallest element we need to do one operation. 
    Hence the total number of operations would be distinct non-zero numbers.
    This type of list comprehension creates a new list and assigns it to the variable.
    """
    nums = [num for num in nums if num != 0]
    return len(set(nums))


# Time Complexity (TC): O(n) | Space Complexity (SC): O(n) | Way of using data structures and in-built func
def minimumOperations(nums: list[int]) -> int:
    return len(set(nums) - {0})
    


# Testing the code
nums = [1,5,0,3,5]
# nums = [0]
print(minimumOperations(nums))
print(minimumOperations_map(nums))
print(minimumOperations_lis(nums))