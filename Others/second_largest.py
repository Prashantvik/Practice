# Find Second largest or Second smallest element in an array
# In case of array contains negative numbers, look at the constraint and take -10e5 or INT_MIN in C++ for max initialize

# Time Complexity (TC): O(nlogn) | Space Complexity (SC): O(1)
def secondlargest_brute(nums : list[int]) -> int:
    nums.sort()
    largest = nums[-1]

    for i in range(len(nums)-1, -1):
        if nums[i] != largest:
            return nums[i]


# Time Complexity (TC): O(2n) | Space Complexity (SC): O(1) | 2 pass algorithm
def secondlargest(nums : list[int]) -> int:
    largest = nums[0]
    slargest = -1

    for num in nums:
        if num > largest:
            largest = num
            
    for num in nums:
        if num > slargest and num != largest:
            slargest = num
        
    return slargest


# Time Complexity (TC): O(n) | Space Complexity (SC): O(1) | Optimal Approach
def secondlargest(nums : list[int]) -> int:
    largest = nums[0]
    slargest = -1

    for num in nums:
        if num > largest:
            slargest = largest 
            largest = num
        elif num < largest and num > slargest:
            slargest = num
    
    return slargest