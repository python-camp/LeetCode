# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
#
# 示例: 
#
# 输入: 13
# 输出: 6
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
#


class Solution(object):
    @staticmethod
    def countDigitOne(n):
        """
        :type n: int
        :rtype: int
        """
        if n > 0:
            for i in range(n+1):
                print(i)


if __name__ == '__main__':
    n = 15
    result = Solution.countDigitOne(n)