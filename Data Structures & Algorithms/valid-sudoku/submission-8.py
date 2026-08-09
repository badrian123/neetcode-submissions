class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #For Row Part
        for row in board:
            seen = set()
            for v in row:
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        
        #For Col Part
        for c in range(len(board)):
            seen = set()
            for r in range(len(board)):
                v = board[r][c]
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        
        #For sub-boxes
        for square in range(9):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c
                    v = board[row][col]
                    if v == ".":
                        continue
                    if v in seen:
                        return False
                    seen.add(v)
        return True

