class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row
        for row in board:
            seen = set()
            for v in row:
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        #Col
        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                v = board[row][col]
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        #9 sub box 3x3
        for subbox in range(9):
            seen = set()
            for row in range(3):
                for col in range(3):
                    r = (subbox // 3) * 3 + row
                    c = (subbox % 3) * 3 + col
                    v = board[r][c]
                    if v == ".":
                        continue
                    if v in seen:
                        return False
                    seen.add(v)
        return True