class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Going to find duplicates in rows and return false if found
        #Going to find duplicates in cols and return false if found
        #Going to find duplicates in subboxes and return false if found
        #Need to account for string "." and numbers
        #Going to use a set in order to keep track of numbers seen and help with identifying duplicates

        #Row
        for row in range(len(board)):
            seen = set()
            for v in board[row]:
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
        #Subbox
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