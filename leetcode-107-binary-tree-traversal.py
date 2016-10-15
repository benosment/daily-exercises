class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        discover = []
        current_level = []
        next_level = []
        answer = []
        if not root:
            return []
        discover.append(root)
        while discover:
            node = discover.pop(0)
            current_level.append(node.val)
            # end of this level
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not discover:
                answer.append(current_level[:])
                current_level = []
                discover = next_level[:]
                next_level = []
        answer.reverse()
        return answer


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)
    print(s.levelOrderBottom(t))
