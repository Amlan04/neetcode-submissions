class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = 9
        sqCheck = [{} for _ in range(9)]
        for i in range(length):
            xCheck,yCheck = {},{}
            for j in range(length):
                if board[i][j] != ".":
                    if board[i][j] in xCheck or board[i][j] in sqCheck[int(i/3)*3+int(j/3)]:
                        return False
                    xCheck[board[i][j]] = j
                    sqCheck[int(i/3)*3+int(j/3)][board[i][j]] = j

                if board[j][i] != ".":
                    if board[j][i] in yCheck:
                        return False
                    yCheck[board[j][i]] = j
        return True