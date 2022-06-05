# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
# 它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，
# 因为3+5+3+8=19。请问该机器人能够到达多少个格子？

class Solution:
    def sums(self, x):
        s = 0
        while x != 0:
            s += x % 10
            x = x // 10
        return s

    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        self.ans = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited:
                return 0
            visited.add((i, j))
            # 这样写会遍历所有的点，因为遇到了不满足K的节点需要直接返回，你这直接向前遍历了
            if self.sums(i) + self.sums(j) <= k:
                self.ans += 1
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)
                # return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
            else:
                return 0

        # return dfs(0, 0)
        dfs(0, 0)
        return self.ans


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            m = 16
            n = 8
            k = 4

            ret = Solution().movingCount(m, n, k)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()