class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #This solves row issue to check for duplicates
        for row in board:
            seen = set()
            for v in row:
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)

        #This solves column issue to check for duplicates
        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                v = board[row][col]
                if v == ".":
                    continue
                elif v in seen:
                    return False
                seen.add(v)
        #Subboxes
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    v = board[row][col]
                    if v == ".":
                        continue
                    elif v in seen:
                        return False
                    seen.add(v)
        return True