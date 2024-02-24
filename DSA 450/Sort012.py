# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
# https://leetcode.com/problems/sort-colors/
# Dutch National Flag Algorithm

"""The Dutch National Flag Algorithm, also known as Dijkstra's three-way partitioning algorithm, is a sorting algorithm designed to efficiently sort an array containing only three unique values, often represented as 0, 1, 2. The goal of the Dutch National Flag Algorithm is to partition the array such that all elements with the value 0 appear before all elements with the value 1, and all elements with the value 1 appear before all elements with the value 2. This sorting is achieved in a single pass through the array, without using any extra space, and with a time complexity of O(n), where n is the number of elements in the array.

The algorithm maintains three pointers:
1. low: Points to the start of the partition containing elements with value 0.
2. mid: Points to the current element being processed.
3. high: Points to the end of the partition containing elements with value 2.

The algorithm iterates through the array from left to right using the mid pointer. At each step, it compares the value of the current element with the values of the elements pointed to by low and high. Depending on the comparison, the algorithm swaps elements to maintain the desired partitioning:

- If nums[mid] is 0, it is swapped with the element pointed to by low, and both low and mid are incremented.
- If nums[mid] is 1, no swapping is required, and mid is incremented.
- If nums[mid] is 2, it is swapped with the element pointed to by high, and high is decremented. However, mid is not incremented in this case because the swapped element needs to be re-evaluated.

The process continues until mid crosses high, indicating that all elements have been processed and the array is partitioned correctly."""

def sortcolors(nums : list[int]) -> None:
    # Variable mid here is the iterator 
    left, mid, right = 0, 0, len(nums)-1
    
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            mid += 1
            left += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[right], nums[mid] = nums[mid], nums[right]
            right -= 1

    print(nums)


# Testing the code
nums = [0,1,2,2,1,0,2,1,1,0,0]
sortcolors(nums)
nums = [2,0,1]
sortcolors(nums)