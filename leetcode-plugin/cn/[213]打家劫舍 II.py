# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。 
#
# 示例 1: 
#
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 
#
# 示例 2: 
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
import logging


class Solution(object):
    @staticmethod
    def rob(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums:
            if len(nums) == 1:
                print(max(nums))

            elif len(nums) == 2:
                print(None)
            else:
                nums_r = nums.copy()
                nums_r.pop(0)
                nums_r.pop()

                if len(nums_r):
                    if len(nums_r) == 2:
                        print(None)
                    rob_list = nums_r[::2]
                    logging.info("rob_list: {}".format(rob_list))
                    print(sum(rob_list))

                logging.info("nums_r: {}".format(nums_r))
            logging.info("nums: {}".format(nums))

        else:
            raise IndexError


if __name__ == '__main__':

    nums = [1, 2, 3]
    result = Solution.rob(nums)

