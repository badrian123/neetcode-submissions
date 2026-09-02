class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Find the target and return true or false if not found
        #Going to need to break down the problem in order to narrow search.
        #Once search narrowed, search in there and return true if found or false when not found.


        #To narrow the search,
            #This is a two dimensional array.
            #Going to need to access the 2d array.
            #Then going to need to check each individual list in 2d array.
                #A short cut would be to check the middle list, the first value, and then decide to check left list or right.
            #Goal is to return a list.
        
        l, r = 0, len(matrix)-1
        while l <= r:
            middle = (l+r) // 2
            if matrix[middle][-1] < target: #Why -1? So checking the ends of the middle to determine where to go.
                l += 1
            elif matrix[middle][0] > target:
                r -= 1
            else:
                break #I see, so we break and no value is temporarily stored.
        
        selected_row = (l+r)//2
        l,r = 0, len(matrix[selected_row]) -1

        while l <=r:
            middle = (l+r) // 2

            if matrix[selected_row][middle] > target:
                r -= 1
            elif matrix[selected_row][middle] < target:
                l += 1
            else:
                return True
        return False