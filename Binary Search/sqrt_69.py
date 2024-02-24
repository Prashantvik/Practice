"""https://leetcode.com/problems/sqrtx/description/"""
"""================================================"""


def mySqrt(n: int) -> int:
    left, right = 1, n+1

    while left < right:
        mid = left + (right - left) // 2
        if mid * mid > n:
            right = mid
        else:
            left = mid + 1
    return left-1 