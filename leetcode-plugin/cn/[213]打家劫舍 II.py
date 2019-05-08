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
            nums_sort = sorted(nums)
            nums_len = len(nums)
            nums_max_len = nums_len // 2
            logging.info("nums_len {}".format(nums_len))
            logging.info("nums_max_len {}".format(nums_max_len))
            logging.info("nums_sort {}".format(nums_sort))
            max_index = - nums_max_len
            logging.info("max_index {}".format(max_index ))
            max_list = []

            for i in range(max_index, 0):
                if i != -1:
                    if nums[i] == nums_sort[i]:
                        i -= 1
                        logging.info("最大值索引 {}".format(i))
                        max_list.append(nums_sort[i])
                        logging.info("最大值list {}".format(max_list))

            logging.info("最大值为：{}".format(max(nums)))
            if max(nums) == nums[0] or max(nums) == nums[-1]:
                if nums[0] > nums[-1]:
                    max_list.append(nums[0])
                else:
                    max_list.append(nums[-1])
                logging.info(max_list)
                rob_list = max_list
                print(sum(rob_list))
        else:
            raise IndexError

        # if nums:
        #     if len(nums) == 1:
        #         print(max(nums))
        #
        #     elif len(nums) == 2:
        #         print(None)
        #         exit(0)
        #     else:
        #         nums_r = nums.copy()
        #         if nums[0] < nums[-1]:
        #             nums_r.pop(0)
        #
        #             if len(nums_r):
        #                 print(nums_r)
        #                 if len(nums_r) == 2:
        #                     print(None)
        #                     exit(0)
        #                 rob_list = nums_r[1::2]
        #                 print("rob_list: {}".format(rob_list))
        #                 print(sum(rob_list))
        #         else:
        #             nums_r.pop()
        #
        #             if len(nums_r):
        #                 print(nums_r)
        #                 if len(nums_r) == 2:
        #                     print(None)
        #                     exit(0)
        #                 rob_list = nums_r[::2]
        #                 print("rob_list: {}".format(rob_list))
        #                 print(sum(rob_list))
        #
        #         logging.info("nums_r: {}".format(nums_r))
        #     logging.info("nums: {}".format(nums))
        #
        # else:
        #     raise IndexError


if __name__ == '__main__':

    nums = [2, 3, 2, 6, 7, 8]
    result = Solution.rob(nums)

