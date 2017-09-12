class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = '0'
        carry = 0
        multi_dict = {0:'0'}
        d = '0'
        for i in range(1, 10):
            d = self.help_add(d, num1, 0) 
            multi_dict[i] = d
        for i in range(len(num2)):
            d_2 = num2[-i - 1]
            multi_res = multi_dict[int(d_2)] + '0' * i
            res = self.help_add(res, multi_res, 0)
        return res

    def help_add(self, num1, num2, carry):
        if num1 and num2:
            d = int(num1[-1]) + int(num2[-1]) + carry
            return self.help_add(num1[:-1], num2[:-1], d // 10) + str(d % 10)
        elif (not num1) and (not num2):
            return '1' if carry == 1 else ''
        elif not num2:
            num2, num1 = num1, num2

        d = int(num2[-1]) + carry
        return self.help_add('', num2[:-1], d // 10) + str(d % 10)
