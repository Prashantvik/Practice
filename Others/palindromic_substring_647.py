
"""https://leetcode.com/problems/palindromic-substrings/description/"""
"""================================================================="""


# On same logic as : longest_palindrome_substr_5.py
# Time Complexity (TC): O(n*n) | Space Complexity (SC): O(n*n)
def countSubstrings(sentence: str) -> int:
    def expand_around_center(left : int, right : int) -> int:
        count_in_range = 0
        while left >= 0 and right < len(sentence) and sentence[left] == sentence[right]:
            left -= 1
            right += 1
            count_in_range += 1
        return count_in_range
    
    count = 0

    for i in range(len(sentence)):
        # Case for odd length palindrome
        odd_palindrome = expand_around_center(i, i)
        count += odd_palindrome

        # Case for even length palindrome
        even_palindrome = expand_around_center(i, i + 1)
        count += even_palindrome
    
    return count




# Testing the code 
strings = "babad"
print(countSubstrings(strings))
s = "abc"
print(countSubstrings(s))