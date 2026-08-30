class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Each row, contains 1-9, without duplicates.
        #Each column, contains 1-9, without duplicates.
        #Each 9 subboxes, contains 1-9, without duplicates.
            #Each subbox is 3 by 3
        #Values are either 1-9 or '.'
        #Input is 2D array.
            #Row = board[row]
            #Colm = board[row][col]
        #Output return true if no duplicates found under above conditions, else return false.

        #Row
            #Each row, contains 1-9, without duplicates.
            #Values are either 1-9 or '.'
            #Output return true if no duplicates found under above conditions, else return false.
        for row in board: #This will give me a list.
            seen = set()
            for v in row: #This will give me value inside of list
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        #Col
            #Colm = board[row][col]
            #Basically do the same thing for row but will need to make sure that column doesn't change every iteration
                #until every row is examined.
        for col in range(len(board)): #1
            seen = set()
            for row in range(len(board)): #1-9
                v = board[row][col]
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        #Subboxes
            #Each 9 subboxes, contains 1-9, without duplicates.
                #Each subbox is 3 by 3
            #Values are either 1-9 or '.'        
        for subbox in range(9):
            #Checking duplicates in subboxes so only keeping track of what's seen per subbox.
            seen = set()
            #Want to check all values in row before moving to next row.
            for row in range(3):
                for col in range(3):
                    #Now how are we going to get the individual value to examine
                    r = (subbox // 3) * 3 + row
                    c = (subbox % 3) * 3 + col
                    v = board[r][c]
                    if v == ".":
                        continue
                    if v in seen:
                        return False
                    seen.add(v)
        return True

