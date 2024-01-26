"""Sort an array which contains only 0,1,2 as element in O(n) TC and O(1) SC"""

def sort_three(nums : list[int]) -> list[int]:
    ones = 0
    twos = 0
    zeros = 0
    numslen = len(nums)

    for number in nums:
        zeros += int(number==0)
        ones  += int(number==1)
        twos  += int(number==2)

    # Shortcut one liner in python
    # Removed 3 while loops for replacing values by this
    nums = [0] * zeros + [1] * ones + [2] * twos
    
    return nums


#Testing the code
nums = [2,1,0,1,2,2,1,0,0,2,1,1,2,0]
print(sort_three(nums))