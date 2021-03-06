#! /usr/bin/env python3


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        while curr.next:
            curr.val = curr.next.val
            if curr.next and curr.next.next:
                curr = curr.next
            else:
                curr.next = None


if __name__ == '__main__':
    pass
