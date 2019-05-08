# coding=utf-8
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
#
# 示例:
#
# 输入: 13
# 输出: 6
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
#


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = []
        for i in range(1, n+1):
            if '1' in str(i):
                L.append(i)
        return len(L)


count = Solution()
print (count.countDigitOne(0))


