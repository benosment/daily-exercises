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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        if head.next == None:
            return False
        reg = head
        fast = head.next
        while reg:
            if reg == fast:
                return True
            reg = reg.next
            if fast:
                fast = fast.next
                if fast:
                    fast = fast.next
        return False

def addLL(head, val):
    node = ListNode(val)
    node.next = head
    return node

if __name__ == '__main__':
    s = Solution()
    l1 = addLL(None, 7)
    l1 = addLL(l1, 3)
    l1 = addLL(l1, 1)
    print(s.hasCycle(l1))
