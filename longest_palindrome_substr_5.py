"""https://leetcode.com/problems/longest-palindromic-substring/description/"""
"""========================================================================"""


# Time Complexity (TC): O(n*n) | Space Complexity (SC): O(n*n)
def longestPalindrome(sentence : str) -> str:
    longest = -1
    longest_substr = ""

    if len(sentence) == 1:
        return sentence

    for i in range(len(sentence)):
        for j in range(i + 1, len(sentence) + 1):
            substr = sentence[i:j]

            if substr == substr[::-1] and len(substr) > longest:
                longest = len(substr)
                longest_substr = substr

    return longest_substr



# Another unique way of thinking
# Time Complexity (TC): O(n*n) | Space Complexity (SC): O(n*n)
def longestPalindrome_unique(sentence: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(sentence) and sentence[left] == sentence[right]:
            left -= 1
            right += 1
        return sentence[left + 1:right]

    longest_substr = ""

    for i in range(len(sentence)):
        # Case for odd length palindrome
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest_substr):
            longest_substr = odd_palindrome

        # Case for even length palindrome
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest_substr):
            longest_substr = even_palindrome

    return longest_substr


# Testing the code 
strings = "babad"
print(longestPalindrome(strings))
print(longestPalindrome_unique(strings))
s = "cbbd"
print(longestPalindrome(s))
print(longestPalindrome_unique(s))