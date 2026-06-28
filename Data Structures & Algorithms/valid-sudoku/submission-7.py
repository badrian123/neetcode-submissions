class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Find duplicates in rows
        for row in board:
            seen = set()
            for v in row:
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        #Find duplicates in col
        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                v = board[row][col]
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        #Find duplicates in subboxes
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3 ) * 3 + i
                    col = (square % 3 ) * 3 + j
                    v = board[row][col]
                    if v == ".":
                        continue
                    if v in seen:
                        return False
                    seen.add(v)
        return True
        