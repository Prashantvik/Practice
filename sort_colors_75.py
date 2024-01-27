"""Sort an array which contains only 0,1,2 as element in O(n) TC and O(1) SC"""

# Time Complexity (TC): O(nc) - Multiple iterations | Space Complexity (SC): O(1)
def sort_three(nums : list[int]) -> list[int]:
    ones = 0
    twos = 0
    zeros = 0
    numslen = len(nums)

    for number in nums:
        zeros += int(number==0)
        ones  += int(number==1)
        twos  += int(number==2)

    # For in place replacement for num values
    idx = 0
    for i in range(zeros):
        nums[idx] = 0
        idx += 1

    for i in range(ones):
        nums[idx] = 1
        idx += 1

    for i in range(twos):
        nums[idx] = 2
        idx += 1
    
    return nums

# Time Complexity (TC): O(n) | Space Complexity (SC): O(1) | Took help 
def sort_three_opt(nums):
    zeros, ones, twos = 0, 0, len(nums) - 1

    # Ones is the iterator and we'll swap zeros and twos with ones
    while ones <= twos:
        if nums[ones] == 0:
            nums[zeros], nums[ones] = nums[ones], nums[zeros]
            zeros += 1
            ones += 1
        elif nums[ones] == 1:
            ones += 1
        else:
            nums[ones], nums[twos] = nums[twos], nums[ones]
            twos -= 1
    
    return nums


#Testing the code
nums = [2, 1, 0, 1, 2, 2, 1, 0, 0, 2, 1, 1, 2, 0]
print(sort_three(nums))
print(sort_three_opt(nums))