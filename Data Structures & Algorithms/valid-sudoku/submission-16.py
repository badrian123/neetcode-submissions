class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Rows no duplicates
        #Col no duplicates
        #9 sub-boxes 3x3 no duplicates

        #Ouput:
            #return true if all conditions met else False
        #1-9 or '.'

        #Given a 2d array.
        #To access row -> board[row]
        #To access col -> board[row][col]
        
        #Row
        #Need to access row.
        #Check all values.
        #store what i've seen.
        #return false if i see a value already seen.

        for row in board:
            seen = set()
            for v in row:
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        #Col
        #We need to stay in one colum, check all the rows, then move to the next col & repeat.
        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                v = board[row][col]
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)        
        #Subboxes
        #Going to examine all 9 subboxes individually.
        #Then we are going to go to the top row.
            #Check all of the column positions. Reset.
            #Then move to the next row & repeat until all areas are examined for duplicates.
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



