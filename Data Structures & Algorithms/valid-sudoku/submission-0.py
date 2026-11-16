class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        rows = [set() for i in range(length)]
        cols = [set() for i in range(length)]
        boxes = [set() for i in range(length)]
        for i in range(length):
            for j in range(length):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in cols[i] or board[i][j] in rows[j] or board[i][j] in boxes[(i//3)*3 + j//3]:
                    return False
                else:
                    cols[i].add(board[i][j])
                    rows[j].add(board[i][j])
                    boxes[(i//3)*3 + j//3].add(board[i][j])

        return True


                