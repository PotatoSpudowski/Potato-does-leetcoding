"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {
            "a",
            "e",
            "i",
            "o",
            "u"
        }
        
        s = list(s)
        ptr_1, ptr_2 = 0, len(s) - 1
        while ptr_1 < ptr_2:
            if s[ptr_1].lower() in vowels and s[ptr_2].lower() in vowels:
                s[ptr_1], s[ptr_2] = s[ptr_2], s[ptr_1]
                ptr_1 += 1
                ptr_2 -= 1
            if s[ptr_1].lower() not in vowels:
                ptr_1 += 1
            if s[ptr_2].lower() not in vowels:
                ptr_2 -= 1
        return ''.join(s)