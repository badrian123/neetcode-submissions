class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Going to need to check for duplicates
        #Handle '.' and numbers
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
                #Col stays the same at zero
                #Row doesn't, it does 0 to 8
                v = board[row][col]
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)

        #Subbox
        for square in range(9):
            seen = set()
            for row in range(3):
                for col in range(3):
                    r = (square // 3 ) * 3 + row
                    c = (square % 3 ) * 3 + col
                    v = board[r][c]
                    if v == ".":
                        continue
                    if v in seen:
                        return False
                    seen.add(v)
        return True

























