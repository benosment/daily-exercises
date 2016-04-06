#!/usr/bin/env python3

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        s = str(self.val)
        if self.next:
            s += '->' + str(self.next)
        return s

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        next_node = None
        while l1 or l2:
            if not l1:
                next_node = l2
                l2 = l2.next
            elif not l2:
                next_node = l1
                l1 = l1.next
            elif l1.val < l2.val:
                next_node = l1
                l1 = l1.next
            else:
                next_node = l2
                l2 = l2.next

            if not head:
                head = next_node
                curr = head
            else:
                curr.next = next_node
                curr = curr.next
        return head


def addLL(head, val):
    node = ListNode(val)
    node.next = head
    return node

if __name__ == '__main__':
    s = Solution()
    l1 = addLL(None, 7)
    l1 = addLL(l1, 3)
    l1 = addLL(l1, 1)
    l2 = addLL(None, 6)
    l2 = addLL(l2, 5)
    l2 = addLL(l2, 4)
    l2 = addLL(l2, 2)
    ans = s.mergeTwoLists(l1, l2)
    print(ans)
