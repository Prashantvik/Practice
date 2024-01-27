"""https://leetcode.com/problems/length-of-last-word/"""
"""=================================================="""

# Time Complexity (TC): O(n*n) | Space Complexity (SC): O(1)
def lenghtOfLastWord(words : str) -> int:
    wordslen = len(words)-1
    last = 0
    flag = False

    while(wordslen > 0):
        if words[wordslen] != ' ':
            flag = True
            last = last + 1
        elif words[wordslen] == ' ' and flag == True:
            return last
        
        wordslen = wordslen - 1
        
    return last



# Testing the code 
words = "Hello World"
words = "luffy is still joyboy"
words = "   fly me   to   the moon  "
print(lenghtOfLastWord(words))