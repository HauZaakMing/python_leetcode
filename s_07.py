from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = preorder[0]
        pos = inorder.index(root)

        n_l = self.buildTree(preorder[1:pos+1],inorder[:pos])
        n_r = self.buildTree(preorder[pos+1:],inorder[pos+1:])
        n = TreeNode(root)
        n.left = n_l
        n.right = n_r
        return n