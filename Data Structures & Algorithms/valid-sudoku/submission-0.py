class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #row
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
        #column
        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in col:
                    return False
                col.add(board[j][i])

        #box (3 x 3)
        for sq in range(9):
            box = set()
            for i in range(3):
                for j in range(3):
                    row = (sq // 3) * 3 + i
                    col = (sq % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in box:
                        return False
                    box.add(board[row][col])

        return True