class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l = sorted(nums1)
        l2 = sorted(nums2)
        i = 0
        j = 0
        ans = []
        while i < len(l) and j < len(l2):
            if l[i] == l2[j]:
                ans.append(l[i])
                i += 1
                j += 1
            elif l[i] > l2[j]:
                j += 1
            else:
                i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 2, 1]
    l2 = [2, 2]
    print(s.intersect(l, l2))
