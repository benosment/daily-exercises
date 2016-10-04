#! /usr/bin/env python3

from itertools import combinations


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        possible_bit_pos = (combinations(range(10), num))
        for possibility in possible_bit_pos:
            bit_array = [0] * 10
            for bitpos in possibility:
                bit_array[bitpos] = 1
            hours = int(''.join([str(bit) for bit in bit_array[:4]]), 2)
            mins = int(''.join([str(bit) for bit in bit_array[4:]]), 2)
            if hours <= 11 and mins <= 59:
                min_string = str(mins)
                if mins < 10:
                    min_string = '0' + min_string
                ans.append('%d:%s' % (hours, min_string))
        return ans


if __name__ == '__main__':
    s = Solution()
    expected_ans = ["0:07", "0:11", "0:13", "0:14", "0:19", "0:21", "0:22", "0:25", "0:26", "0:28", "0:35", "0:37",
                    "0:38", "0:41", "0:42", "0:44", "0:49", "0:50", "0:52", "0:56", "1:03", "1:05", "1:06", "1:09",
                    "1:10", "1:12", "1:17", "1:18", "1:20", "1:24", "1:33", "1:34", "1:36", "1:40", "1:48", "2:03",
                    "2:05", "2:06", "2:09", "2:10", "2:12", "2:17", "2:18", "2:20", "2:24", "2:33", "2:34", "2:36",
                    "2:40", "2:48", "3:01", "3:02", "3:04", "3:08", "3:16", "3:32", "4:03", "4:05", "4:06", "4:09",
                    "4:10", "4:12", "4:17", "4:18", "4:20", "4:24", "4:33", "4:34", "4:36", "4:40", "4:48", "5:01",
                    "5:02", "5:04", "5:08", "5:16", "5:32", "6:01", "6:02", "6:04", "6:08", "6:16", "6:32", "7:00",
                    "8:03", "8:05", "8:06", "8:09", "8:10", "8:12", "8:17", "8:18", "8:20", "8:24", "8:33", "8:34",
                    "8:36", "8:40", "8:48", "9:01", "9:02", "9:04", "9:08", "9:16", "9:32", "10:01", "10:02", "10:04",
                    "10:08", "10:16", "10:32", "11:00"]
    my_ans = s.readBinaryWatch(3)
    for a in my_ans:
        if a not in expected_ans:
            print('not in - %s' % a)
        else:
            expected_ans.remove(a)
    print('leftover')
    print(expected_ans)
