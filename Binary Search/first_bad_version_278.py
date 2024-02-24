"""https://leetcode.com/problems/first-bad-version/description/"""
"""============================================================"""



def isBadVersion(version : int) -> bool:
    pass

# Time Complexity (TC): O(logn) | Space Complexity (SC): O(1)
def firstBadVersion(self, n) -> int:
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left