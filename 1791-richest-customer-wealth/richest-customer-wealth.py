class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])
        max = 0
        for i in range(m):
            a = 0
            for j in range(n):
                a += accounts[i][j]
            if a > max:
                max = a

        return max
