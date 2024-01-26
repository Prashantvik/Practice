"""https://leetcode.com/problems/set-mismatch/description/"""
"""======================================================="""

# TC : O(n) | SC : O(n) Constant
def mismatch_hashmap(nums : list[int]) -> list[int]:
    numslen = len(nums)
    actual_sum = int(numslen*(numslen+1)/2)
    current_sum = sum(nums)
    extra = 0

    #Hashmap implementation
    map = {}
    for num in nums:
        if num not in map.keys():
            map[num] = 1
        else:
            map[num] += 1
        if map[num] == 2:
            extra = num
            break
         
    return [extra, actual_sum-(current_sum-extra)]


# TC : O(nlogn) | SC : O(1) Constant
def mismatch_sort(nums : list[int]) -> list[int]:
    numslen = len(nums)
    extra = -1
    actual_sum = int(numslen*(numslen+1)/2)
    current_sum = sum(nums)
    nums.sort()

    for i in range(numslen-1):
        if nums[i] == nums[i+1]:
            extra = nums[i]
            break
        
    return [extra, actual_sum-(current_sum-extra)]

# Testing the actual code
nums = [1,1]
print(mismatch_hashmap(nums))
print(mismatch_sort(nums))