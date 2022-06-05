import json
import random
from typing import *
"""
剑指offer 45
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
"""

class Solution:
    def compare(self, x: int, y: int) -> bool:
        if int(str(x) + str(y)) > int(str(y) + str(x)):
            # x > y return True
            return True
        else:
            return False

    def sort_onetime(self, nums: List[int], low: int, high: int) -> int:
        pivot_pos = random.randint(low, high)
        pivot = nums[pivot_pos]
        nums[low], nums[pivot_pos] = nums[pivot_pos], nums[low]
        while low < high:
            while not self.compare(nums[high], pivot) and low < high:
                high -= 1
            nums[high], nums[low] = nums[low], nums[high]
            while self.compare(nums[low], pivot) and low < high:
                low += 1
            nums[low], nums[high] = nums[high], nums[low]
        nums[low] = pivot
        return low

    def quick_sort(self, nums: List[int], low: int, high: int):
        if low >= high:
            return
        pivot_pos = self.sort_onetime(nums, low, high)
        self.quick_sort(nums, low, pivot_pos - 1)
        self.quick_sort(nums, pivot_pos + 1, high)

    def minNumber(self, nums: List[int]) -> str:
        self.quick_sort(nums, 0, len(nums) - 1)
        s = ""
        for num in nums:
            s += str(num)
        return s


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    # lines = readlines()

    # line = next(lines)
    nums = [3, 30, 34, 5, 9]

    ret = Solution().minNumber(nums)

    print(ret)



if __name__ == '__main__':
    main()