#! /usr/bin/env python3

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        for i, starting_letter in enumerate(s):
            seen = {}
            seen[starting_letter] = 1
            length = 1
            for letter in s[i+1:]:
                if letter in seen:
                    break
                else:
                    seen[letter] = 1
                    length += 1
            if length > max_length:
                max_length = length
        return max_length

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbbabcd'))
    print(s.lengthOfLongestSubstring('bbbbbb'))
    print(s.lengthOfLongestSubstring('s'))
    print(s.lengthOfLongestSubstring('au'))
