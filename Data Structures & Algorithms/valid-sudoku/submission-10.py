class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #For row Part
            for row in board:
                seen = set()
                for v in row:
                    if v == ".":
                        continue
                    if v in seen:
                        return False
                    seen.add(v)                    
        #For col Part
            for col in range(len(board)):
                seen = set()
                for row in range(len(board)):
                    v = board[row][col]
                    if v == ".":
                        continue
                    if v in seen:
                        return False
                    seen.add(v)
        #For Sub Box Part
            for square in range(9):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        row = (square //3 )*3 + r
                        col = (square % 3)*3 + c
                        v = board[row][col]
                        if v == ".":
                            continue
                        if v in seen:
                            return False
                        seen.add(v)
            return True