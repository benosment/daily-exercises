# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sum_left_leaves_helper(root, False)

    def sum_left_leaves_helper(self, node, left_child):
        if node == None:
            return 0
        if node.right == None and node.left == None:
            if left_child:
                return node.val
            else:
                return 0
        else:
            return self.sum_left_leaves_helper(node.left, True) + self.sum_left_leaves_helper(node.right, False)


if __name__ == '__main__':
    s = Solution()
