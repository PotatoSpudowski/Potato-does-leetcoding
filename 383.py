"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        dic = {}
        for i in magazine:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
                
                
        for i in ransomNote:
            if i not in dic or dic[i] < 1:
                return False
            else:
                dic[i]-=1
                
        return True
        