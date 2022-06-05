import random
from typing import *
import json

# 双指针快速排序
class Solution_1:
    def sort_onetime(self, nums, l, r):
        #  改进版本，随机选择pivot
        pivot = random.randint(l, r)
        nums[pivot], nums[l] = nums[l], nums[pivot]
        pivot = nums[l]
        # 原始版本 选择最左的元素作为pivot
        # pivot = nums[l]
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] < pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l

    def quick_sort(self, nums, l, r):
        if l>=r:
            return
        pivot_pos = self.sort_onetime(nums, l, r)
        self.quick_sort(nums, l, pivot_pos - 1)
        self.quick_sort(nums, pivot_pos + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums


class Solution_2:
    def sort_onetime(self, nums, l, r):
        pivot = nums[r]
        low = l - 1
        high = l
        while high <= r-1:
            if nums[high] < pivot:
                low += 1
                self.swap(nums, low, high)
            high += 1
        low += 1
        self.swap(nums, low, r)
        return low


    def swap(self, nums, low, high):
        temp = nums[low]
        nums[low] = nums[high]
        nums[high] = temp


    def quick_sort(self, nums, l, r):
        if l>=r:
            return
        pivot_pos = self.sort_onetime(nums, l, r)
        self.quick_sort(nums, l, pivot_pos-1)
        self.quick_sort(nums, pivot_pos+1, r)


    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    nums = [5, 2, 3, 1]
    ret = Solution_2().sortArray(nums)
    print(ret)


if __name__ == '__main__':
    main()
