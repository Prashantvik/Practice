# Leetcode Article Link
[Python Powerful Ultimate Binary Search Template](https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)

## Most Generalized Binary Search
Suppose we have a search space. It could be an array, a range, etc. Usually, it's sorted in ascending order. For most tasks, we can transform the requirement into the following generalized form:

**Minimize k , s.t. condition(k) is True**

The following code is the most generalized binary search template:

```python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space)  # could be [0, n], [1, n] etc. Depends on the problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```
What's really nice about this template is that, for most of the binary search problems, we only need to modify three parts after copy-pasting this template and never need to worry about corner cases and bugs in code anymore:

1. Correctly initialize the boundary variables left and right to specify the search space. Only one rule: set up the boundary to include all possible elements;
2. Decide the return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal k satisfying the condition function;
3. Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

## Advanced Application
The above problems are quite easy to solve, because they already give us the array to be searched. We'd know that we should use binary search to solve them at first glance. However, more often are the situations where the search space and search target are not so readily available. Sometimes we won't even realize that the problem should be solved with binary search -- we might just turn to dynamic programming or DFS and get stuck for a very long time.

**As for the question "When can we use binary search?", my answer is that, If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.**