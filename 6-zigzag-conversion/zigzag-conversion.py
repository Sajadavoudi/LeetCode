class Solution:
    def convert(self, s: str, numRows: int) -> str:
        m = len(s)
        if m <= numRows or numRows == 1:
            return s
        else:
            result = ""
            for i in range(numRows):
                for j in range(i, m,(numRows-1)*2):
                    result += s[j]
                    if (i > 0 and i < numRows - 1 and j + (numRows-1)*2 -2*i < m):
                        result += s[j + (numRows-1)*2 -2*i]

        return result

        