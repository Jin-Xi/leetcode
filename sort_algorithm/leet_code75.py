import random
from typing import *
import json


class Solution:
    # 单指针，双遍历
    def sortColors_1(self, nums: List[int]) -> None:
        length = len(nums)
        ptr = -1
        for index in range(0, length):
            if nums[index] == 0:
                ptr += 1
                nums[ptr], nums[index] = nums[index], nums[ptr]
        for index in range(ptr + 1, length):
            if nums[index] == 1:
                ptr += 1
                nums[ptr], nums[index] = nums[index], nums[ptr]

        return nums

    # 双指针，单遍历
    def sortColors_2(self, nums: List[int]) -> None:
        length = len(nums)
        p0 = -1
        p1 = -1

        for index in range(0, length):
            if nums[index] == 0:
                if p0 == p1:
                    p0 += 1
                    p1 += 1
                    nums[p0], nums[index] = nums[index], nums[p0]
                else:
                    p0 += 1
                    nums[p0], nums[index] = nums[index], nums[p0]
                    p1 += 1
                    nums[p1], nums[index] = nums[index], nums[p1]
            elif nums[index] == 1:
                p1 += 1
                nums[p1], nums[index] = nums[index], nums[p1]
        return nums

    # 双指针2
    def sortColors(self, nums: List[int]) -> None:
        length = len(nums)
        p0 = -1
        p2 = length
        index = 0
        while p2 > index:
            if nums[index] == 0:
                p0 += 1
                nums[p0], nums[index] = nums[index], nums[p0]
            elif nums[index] == 1:
                p2 -= 1
                nums[p2], nums[index] = nums[index], nums[p2]

            index += 1
        return nums



def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    nums = [2,0,2,1,1,0]
    ret = Solution().sortColors(nums)
    print(ret)


if __name__ == '__main__':
    # main()
    print('b'-'a')