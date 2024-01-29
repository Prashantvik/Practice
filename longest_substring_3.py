"""https://leetcode.com/problems/longest-substring-without-repeating-characters/description/"""
"""========================================================================================="""


# Time Complexity (TC): O(n*n) | Space Complexity (SC): O(n)
def lengthOfLongestSubstring(strings: str) -> int:
        if len(strings) < 1:
            return 0

        longest = 0

        for i in range(len(strings)):
            char_map = {}
            current_length = 0

            for k in range(i, len(strings)):
                if strings[k] in char_map:
                    break
                char_map[strings[k]] = 1
                current_length += 1

            longest = max(longest, current_length)

        return longest


# Time Complexity (TC): O(n) | Space Complexity (SC): O(n) | Two pointers and Hashmap
def lengthOfLongestSubstring_opt(longstr: str) -> int:
        longest  = 0
        map_char = {}
        start = 0

        for i in range(len(longstr)):
            if map_char and longstr[i] in map_char:
                if map_char[longstr[i]] >= start:
                    start = map_char[longstr[i]] + 1
                
            map_char[longstr[i]] = i
            longest = max(longest, i - start + 1)
        
        return longest


# Testing the code
s = "abcabcbb"
print(lengthOfLongestSubstring_opt(s))
print(lengthOfLongestSubstring(s))