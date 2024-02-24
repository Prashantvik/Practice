"""https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/"""
"""================================================================================"""

# Time Complexity (TC): O(n) | Space Complexity (SC): O(n)
def findArray(pref: list[int]) -> list[int]:
        """
        Read and pratice on bitwise operator, basics, properties and techniques
        """
        ans = []
        ans.append(pref[0])

        for i in range(1, len(pref)):
            ans.append(pref[i-1] ^ pref[i])
        
        return ans


# Testing the code
pref = [5,2,0,3,1]
print(findArray(pref))