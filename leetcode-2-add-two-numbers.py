#! /usr/bin/env python3

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = False
        answer = None
        head = None
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val
            elif l1:
                val = l1.val
            else:
                val = l2.val
            if carry:
                val += 1
            if val >= 10:
                carry = True
                val = val % 10
            else:
                carry = False

            l = ListNode(val)
            if not answer:
                answer = l
                head = answer
            else:
                head.next = l
                head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            l = ListNode(1)
            head.next = l
            head = head.next
        return answer


if __name__ == '__main__':
    l1 = None
    l2 = None
    for i in [1]:
        l = ListNode(i)
        l.next = l1
        l1 = l
    for i in [9,9]:
        l = ListNode(i)
        l.next = l2
        l2 = l
    s = Solution()
    a = s.addTwoNumbers(l1, l2)
