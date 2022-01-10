import copy
from typing import List, Optional
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # self.flag = 0
        output = []
        def dfs(row, col):
            if row > 8:
                output.append(copy.deepcopy(board))
                return
            if col > 8:
                dfs(row + 1, 0)
            elif board[row][col] == '.':
                for i in range(1, 10):
                    if isOk(row, col, str(i)):
                        board[row][col] = str(i)
                        dfs(row, col + 1)
                        board[row][col] = '.'
            else:
                dfs(row, col + 1)
        def isOk(row, col, num):
            for i in range(9):
                if board[i][col] == num:
                    return False
                if board[row][i] == num:
                    return False
            cellR = row // 3
            cellC = col // 3
            for i in range(cellR * 3, cellR * 3 + 3):
                for j in range(cellC * 3, cellC * 3 + 3):
                    if board[i][j] == num:
                        return False
            return True
        dfs(0, 0)
        self.show([board])
        self.show(output)
    def show(self, output):

        for k in range(len(output)):
            print('solution', k + 1)
            print('——————————————————————————————————')
            it = output[k]
            for i in range(9):
                for j in range(9):
                    if j == 0:
                        print('｜ ',end = '')
                    if (j + 1)%3 == 0:
                        print(it[i][j],end = ' ｜ ')
                    else:
                        print(it[i][j], end='  ')
                if (i + 1)%3 == 0:
                    print()
                    print('——————————————————————————————————')

                else:
                    print()
s = Solution()
board = [["5","9",".","6",".","4",".",".","."],
         [".",".",".","9",".",".","5",".","."],
         ["8",".",".",".","5","7","6",".","9"],
         [".",".","5",".",".",".","4",".","6"],
         [".",".",".","7","4",".","2",".","."],
         ["2",".","8",".",".",".",".","5","."],
         [".",".",".","5",".",".",".","7","."],
         [".",".","1",".","7",".","9",".","."],
         ["7","3","6",".","2",".",".",".","."]]
s.solveSudoku(board)