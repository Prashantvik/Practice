"""https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/"""
"""=================================================================================="""

def shipWithinDays(self, weights: list[int], days: int) -> int:
    def feasible(capacity : int) -> bool:
        total = 0 
        day = 1
        for weight in weights:
            total += weight
            if total > capacity: # Exceeded one day capacity
                total = weight
                day += 1
                if day > days:   # Given days exceeded
                    return False
        return True


    left, right = max(weights), sum(weights)
    while(left < right):
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    
    return left