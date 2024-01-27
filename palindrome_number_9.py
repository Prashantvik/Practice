"""https://leetcode.com/problems/palindrome-number/description/"""
"""============================================================"""

# Time Complexity (TC): O(n) | Space Complexity (SC): O(1)
def isPalindrome(x: int) -> bool:
        # Elimination of edge cases
        if(x<0 or (x!=0 and x%10==0)):
            return False
        rev = 0
        newx = x
        
        # Create the reverse of number
        while x>0:
            rem = x%10
            rev = rev*10 + rem
            x = x//10
        
        return (newx==rev or rev/10==newx)


# Testing the code
num = 1211121
print(isPalindrome(num))