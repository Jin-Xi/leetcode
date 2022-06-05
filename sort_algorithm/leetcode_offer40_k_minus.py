import json
import random
from typing import *


class Solution:
    def swap(self, nums, low, high):
        temp = nums[low]
        nums[low] = nums[high]
        nums[high] = temp


    # def partition(self, nums, low, high):
    #     pivot_pos = random.randint(low, high)
    #     pivot = nums[pivot_pos]
    #     nums[pivot_pos], nums[low] = nums[low], nums[pivot_pos]
    #     while low < high:
    #         while nums[high] >= pivot and low < high:
    #             high -= 1
    #         nums[low] = nums[high]
    #         while nums[low] < pivot and low < high:
    #             low += 1
    #         nums[high] = nums[low]
    #     nums[low] = pivot
    #     return low


    # def partition(self, nums, l, r):
    #     pivot = nums[r]
    #     low = l - 1
    #     high = l
    #     while high <= r-1:
    #         if nums[high] < pivot:
    #             low += 1
    #             self.swap(nums, low, high)
    #         high += 1
    #     low += 1
    #     self.swap(nums, low, r)
    #     return low


    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1


    def get_k(self, nums, low, high, k):
        if low >= high:
            return
        pos = self.partition(nums, low, high)
        # 需要考虑ｋ>pos的情况，此时递归的右边界会变化，所以要截去ｌｏｗ到ｐｏｓ的位置
        offset = pos - low + 1
        if offset == k:
            return
        if offset < k:
            self.get_k(nums, low, pos-1, k)
        else:
            self.get_k(nums, pos+1, high, k-offset)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        self.get_k(arr, 0, len(arr)-1, k)
        return arr[:k]


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    arr = [0,1,1,2,4,4,1,3,3,2]

    k = 6

    ret = Solution().getLeastNumbers(arr, k)

    print(ret)


if __name__ == '__main__':
    main()