class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            for j in range(i+1, len(nums)):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

    def move_zeroes_alt(self, nums):
        curr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curr] = nums[i]
                curr += 1
        for i in range(curr, len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    s = Solution()
    l = [0, 1, 0, 3, 12]
    s.move_zeroes_alt(l)
    print(l)
