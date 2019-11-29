"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        
        s = s.lower()
        i, j = 0, len(s)-1
        
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            elif s[i].isalnum():
                j-=1
            elif s[j].isalnum():
                i+=1
            else:
                i+=1
                j-=1
                
        return True
        
        