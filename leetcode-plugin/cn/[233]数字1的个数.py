# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
#
# 示例: 
#
# 输入: 13
# 输出: 6
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
#
import logging


class Solution(object):
    @staticmethod
    def countDigitOne(n):
        """
        :type n: int
        :rtype: int
        """
        contain_list = []
        if n > 0:
            for i in range(n+1):
                # print(i)
                contain_str = "1"
                if contain_str in str(i):
                    logging.info(i)
                    contain_list.append(i)
            logging.info(contain_list)
            print(len(contain_list))


if __name__ == '__main__':
    n = 19
    result = Solution.countDigitOne(n)
