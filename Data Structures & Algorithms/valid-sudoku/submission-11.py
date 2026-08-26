class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #I know that I have to solve for column, row, & subbox
        #I am going to use a set in order to keep track of what was seen.
        #It's going to be three sections of code.
        #Row and Column should be easiest.
        #Subbox it is going to require,
            #A range of 9 because there is that many
            #Then three iteration top to bottom
                #Inside:
                    #Three iteration left to right
        
        #Range
        for row in range(len(board)):
            seen = set()
            for v in board[row]:
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)        
        #Column
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
        #So I have 9 squares.
            #I need to iterate through the sections.
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