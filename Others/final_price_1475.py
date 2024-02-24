"""https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/"""
"""========================================================================================="""

# Time Complexity (TC): O(n*n) | Space Complexity (SC): O(n)
def final_prices(prices : list[int]) -> list[int]:

    for i in range(len(prices)):
        for k in range(i+1, len(prices)):
            if prices[i] >= prices[k]:
                prices[i] = prices[i] - prices[k]
                break
    
    return prices


# Time Complexity (TC): O(n*n) | Space Complexity (SC): O(1)
def final_prices_new(prices : list[int]) -> list[int]:

    for i in range(len(prices)-1):
        k = i+1
        while(k < len(prices)):
            if (prices[i] >= prices[k]):
                prices[i] = prices[i] - prices[k]
                break
            k += 1
    
return prices


# Time Complexity (TC): O(n*n) | Space Complexity (SC): O(n) | Not able to optimise, help
def final_prices_opt(prices : list[int]) -> list[int]:
    """
    Problem of stack, must know the data structures before I solve more problems. Monotone stack. The main idea is to use 
    a stack to keep track of the indices of prices that need to be processed. This way, we can avoid unnecessary nested loops.
    """
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            popped_index = stack.pop()
            prices[popped_index] -= prices[i]

        stack.append(i)

    return prices



# Testing the actual code
# These are doing in place so don't run these continue
prices = [8,4,6,2,3]
# print(final_prices_opt(prices))
# print(final_prices(prices))       
print(final_prices_new(prices))