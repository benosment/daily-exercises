class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = ''
        carry = 0
        while num1 or num2:
            if not num1:
                inter_sum = int(num2[-1]) + carry
                num2 = num2[:-1]
            elif not num2:
                inter_sum = int(num1[-1]) + carry
                num1 = num1[:-1]
            else:
                inter_sum = int(num1[-1]) + int(num2[-1]) + carry
                print(inter_sum, int(num1[-1]), int(num2[-1]), carry)
                num1 = num1[:-1]
                num2 = num2[:-1]
            if inter_sum >= 10:
                new_sum = inter_sum % 10
                carry = int((inter_sum - new_sum) / 10)
                inter_sum = new_sum
            else:
                carry = 0
            ans = str(inter_sum) + ans
        if carry:
            ans = str(carry) + ans
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.addStrings("123456789", "987654321"))
