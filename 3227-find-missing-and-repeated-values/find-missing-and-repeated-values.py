class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hash = {} # map the number to repition
        sum = 0
        double = 0
        n = len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum += grid[i][j]
                if grid[i][j] not in hash:
                    hash[grid[i][j]] = 1
                else:
                    hash[grid[i][j]] += 1
                    double = grid[i][j]

        should_sum = (n**2 * (n**2 + 1)) // 2
        miss = double + should_sum - sum
        return [double, miss]
