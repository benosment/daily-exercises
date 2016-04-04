class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen_so_far = {}
        for num in nums:
            seen_so_far[num] = seen_so_far.get(num, 0) + 1
            if seen_so_far[num] > 1:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,2,3,4]))
    print(s.containsDuplicate([1,2,3,4,
