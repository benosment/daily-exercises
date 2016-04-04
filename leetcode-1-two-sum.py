#! /usr/bin/env python3

'''
Given an array of integers, find two numbers such that they add up to
a specific target number.

The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than
index2. Please note that your returned answers (both index1 and
index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9 Output: index1=1, index2=2
'''

# could do it with one loop

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for (i, val) in enumerate(nums):
            need = target - val
            if need in hashmap:
                return [hashmap[need] + 1, i + 1]
            hashmap[val] = i


if __name__ == '__main__':
    s = Solution()
    #print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([0,4,3,0], 0))
