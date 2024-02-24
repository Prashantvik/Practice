"""https://leetcode.com/problems/valid-palindrome/"""
"""==============================================="""

# Time Complexity (TC): O(n) | Space Complexity (SC): O(n)
def isPalindrome(sentence: str) -> bool:
    cleaned_string = ''.join(char for char in sentence.lower() if char.isalpha() or char.isnumeric())

    return cleaned_string == cleaned_string[::-1]


# Time Complexity (TC): O(n) | Space Complexity (SC): O(1) | Two pointers approach
# Was able to come up with logic, implementation issue in "use continue" to skip the below code **
def isPalindrome_opt(sentence: str) -> bool:
    start = 0
    end = len(sentence) - 1

    while start < end:
        if sentence[start].isalnum():
            start_char = sentence[start].lower()
        else:
            start += 1
            continue

        if sentence[end].isalnum():
            end_char = sentence[end].lower()
        else:
            end -= 1
            continue
        
        if start_char != end_char:
            return False

        start += 1
        end -= 1

        return True


# Testing the code
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
print(isPalindrome_opt(s))