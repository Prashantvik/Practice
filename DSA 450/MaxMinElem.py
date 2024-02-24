# Find the maximum and minimum element in an array
# Constrains - element can be negative and positive

def maxmin(nums : list[int]) -> list[int]:
    maxelem = -10e5
    minelem = 10e5

    for elem in nums:
        if elem > maxelem:
            maxelem = elem
        if elem < minelem:
            minelem = elem
    
    return [minelem, maxelem]


# Testing the code
nums = [-1,2,3,5,6,8,9,-10]
print(maxmin(nums))