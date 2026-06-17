class Solution:
    def isValidGrid(self, board: list[list[str]]) -> bool:
        #Check the height:
        if len(board) != 9:
            return False
        #Check the length of each array
        for row in board:
            if len(row) != 9:
                return False
        return True
    def checkRowsForDuplicate(self, board: list[list[str]])-> bool:
        for row in board:
            numsChecked = set()
            for i in row:
                if i != ".":
                    if int(i) not in numsChecked:
                        numsChecked.add(int(i))
                    else:
                        return False
        return True
    def checkColumnsForDuplicate(self, board: list[list[str]])-> bool:
        for i in range(len(board)):
            numsChecked = set()
            for j in range(len(board[i])):
                value = board[j][i]
                if value != ".":
                    if value not in numsChecked:
                        numsChecked.add(value)
                    else:
                        return False
        return True
    def checkSubBox(self, board: list[list[str]])-> bool:
        x1 = 0
        x2 = 3
        y1 = 0
        y2 = 3
        for j in range(3):
            for i in range(3):
                checkedNum = set()
                for row in range(y1,y2, 1):
                    for column in range(x1, x2, 1):
                        if board[row][column] != ".":
                            if int(board[row][column]) not in checkedNum:
                                checkedNum.add(int(board[row][column]))
                            else:
                                return False
                x1 += 3
                x2 += 3
            y1 += 3
            y2 += 3
            x1 = 0
            x2 = 0
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.isValidGrid(board):
            if self.checkRowsForDuplicate(board):
                if(self.checkColumnsForDuplicate(board)):
                    if(self.checkSubBox(board)):
                        return True
        return False