class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        majority_threshold = int(len(nums) / 2)
        for elem in nums:
            counts[elem] = counts.get(elem, 0) + 1
            if counts[elem] > majority_threshold:
                return elem
