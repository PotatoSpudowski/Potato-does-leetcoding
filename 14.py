"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        pstr = strs[0]
        for i in range(1,len(strs)):
            split = 0
            for j in range(min(len(strs[i]),len(pstr))):
                if pstr[j] == strs[i][j]:
                    split+=1  
                else:
                    break
                    
            pstr = pstr[:split]
            
        return pstr