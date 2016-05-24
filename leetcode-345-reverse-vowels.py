class Solution(object):
    def __init__(self):
        self.VOWELS = "aeiouAEIOU"

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_in_word = []
        new_word = list(s)
        for letter in s:
            if letter in vowels:
                vowels_in_word.append(letter)
        j = len(vowels_in_word) - 1
        for (i, letter) in enumerate(s):
            if letter in vowels:
                new_word[i] = vowels_in_word[j]
                j -= 1
        return ''.join(new_word)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels("hello"))
    print(s.reverseVowels("leetcode"))
