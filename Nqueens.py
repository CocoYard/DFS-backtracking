from typing import List, Optional

class Solution:
    @staticmethod
    def solveNQueens( n: int):
        m = [[0] * n for _ in range(n)]

        def btQ(row):
            if row == n:
                return [[]]
            res = []
            for i in range(n):
                if isOK(row, i):
                    placeQ(row, i)
                    temp = ""
                    for _ in range(n):
                        temp += '_  '
                    temp = temp[:3*i] + "Q" + temp[3*i + 1:]
                    res += [[temp] + _ for _ in btQ(row + 1)]
                    removeQ(row, i)
            return res

        def placeQ(row, col):
            m[row][col] = 1

        def isOK(row, col):
            for i in range(n):
                if m[i][col]:
                    return False
            i, j = row, col
            while 0 <= i < n and 0 <= j < n:
                if m[i][j]:
                    return False
                i -= 1
                j -= 1
            i, j = row, col
            while 0 <= i < n and 0 <= j < n:
                if m[i][j]:
                    return False
                i -= 1
                j += 1
            return True

        def removeQ(row, col):
            m[row][col] = 0

        return btQ(0)
res = Solution.solveNQueens(5)
for it in res:
    for i in it:
        print(i)
    print("#############")