class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_count = {}
        for letter in magazine:
            magazine_count[letter] = magazine_count.get(letter, 0) + 1
        for letter in ransomNote:
            if letter not in magazine_count:
                return False
            if magazine_count[letter] == 0:
                return False
            magazine_count[letter] -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct("a", "b"))
    print(s.canConstruct("aa", "ab"))
    print(s.canConstruct("aa", "aab"))
