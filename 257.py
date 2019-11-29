"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        def dfs(roots, path, paths):
            path += str(roots.val)
            if not roots.left and not roots.right:
                paths.append(path)
                return
            
            if roots.left:
                dfs(roots.left, path + "->", paths)
                    
            if roots.right:
                dfs(roots.right, path + "->", paths)
                    
        paths = []
        path = ""
        if not root:
            return paths
        
        dfs(root, path, paths)
        return paths