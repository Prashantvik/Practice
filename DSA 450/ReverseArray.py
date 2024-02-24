# Reverse the array
# Two pointers approach

def reverse(nums : list[int]) -> list[int]:
    start = 0
    end = len(nums)-1

    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start = start + 1
        end = end - 1
    
    return nums



# Testing the code
nums = [1,2,3,5,6,8,9,10]
print(reverse(nums))