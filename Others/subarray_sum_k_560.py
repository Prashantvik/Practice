"""https://leetcode.com/problems/subarray-sum-equals-k/description/"""
"""================================================================"""

# Time Complexity (TC): O(n) | Space Complexity (SC): O(n) | Hashmap
def subarraySum(nums : list[int], k: int) -> int:
        count = 0
        prefix_sum  = 0
        # Initializing for the case when k == prefix_sum
        sum_map = {0 : 1}

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in sum_map:
                count += sum_map[prefix_sum - k]

            if prefix_sum in sum_map:
                sum_map[prefix_sum] += 1
            else:
                sum_map[prefix_sum] = 1

        return count


# Testing the code
nums = [1,1,1]
k = 2
print(subarraySum(nums, k))