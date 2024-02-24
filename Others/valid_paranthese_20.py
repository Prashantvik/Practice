"""https://leetcode.com/problems/valid-parentheses/description/"""
"""============================================================"""


# Time Complexity (TC): O(n) | Space Complexity (SC): O(N) 
# Able to come up with logic, minor issue | Appending is stack
def isValid(parentheses: str) -> bool:
    para_dict = {'(' : ')', '{' : '}', '[' : ']'}
    stack = []

    for elem in parentheses:
        if elem in para_dict:
            stack.append(elem)
        elif stack and para_dict[stack[-1]] == elem:
            stack.pop()
        else:
            return False

    return not stack


# Time Complexity (TC): O(n) | Space Complexity (SC): O(N) 
def isValid(parentheses: str) -> bool:
    para_dict = {')': '(', '}': '{', ']': '['}
    stack = []

    for elem in parentheses:
        if elem in para_dict.values():  
        # Check if the character is an opening parenthesis
            stack.append(elem)
        elif stack and para_dict[elem] == stack[-1]:  
        # Check if the character matches the top of the stack
            stack.pop()
        else:
            return False

    return not stack

# Testing the code
s = "()[]{}"
s = "({[)]}"
print(isValid(s))