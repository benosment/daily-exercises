class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return lca(root, p, q)

def lca(node, p, q):
    if not node:
        return None
    if p.val > q.val:
        p, q = q,p
    if p.val <= node.val <= q.val:
        return node
    elif p.val > node.val:
        return lca(node.right, p, q)
    else:
        return lca(node.left, p, q)
