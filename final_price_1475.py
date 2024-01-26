"""https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/"""
"""========================================================================================="""

# TC : O(n^2) | SC : O(n)
def final_prices(prices : list[int]) -> list[int]:
    answer = prices

    for i in range(len(prices)):
        for k in range(i+1, len(prices)):
            if answer[i] >= answer[k]:
                answer[i] -= answer[k]
                break
    
    return answer



# Testing the actual code
nums = [8,4,6,2,3]
print(final_prices(nums))