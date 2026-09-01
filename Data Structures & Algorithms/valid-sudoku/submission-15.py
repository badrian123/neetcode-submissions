class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row, Col, subboxes without duplicates.
        #Given a 2D array.
        #Strings in 1-9 or '.'

        #row = board[row]
        #col = board[row][col]
        #v = board[row][col]

        #First I need to check if there are any duplicates in the row and the other rows too:
        #I will just iterate through the 2d array and use it's first position in order to examine the values in every row.
        #Going to use a set in order to keep track of the values already seen.
        #Then going to be using comparisons in order to determine if duplicate exist based on if the value has already been seen.

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
        #I know that I am going to have to iterate through all of the rows while checking the same column position.
        #So col = board[row][col]
        #I am going to create a for loop and set that to my column. That way the value doesn't change until all rows have been examined.
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
        #there's 9 subboxes
        #Going to be examining three 3 rows
        #In every row, going to be examining 3 columns

        for subbox in range(9):
            #Going to need to keep track of what's been seen per subbox
            seen = set()
            #Since we are checking row firsts before columns we will set it as our first for loop
            for row in range(3):
                for col in range(3):
                    #Now need to examine the individual values.
                    r = (subbox // 3) * 3 + row
                    c = (subbox % 3) * 3 + col
                    v = board[r][c]
                    if v == ".":
                        continue
                    if v in seen:
                        return False
                    seen.add(v)
        return True
