class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Given an array
        #replace every element in that array with the greatest element among the elements to its right
        #replace the last element with -1

        #Brainstorm:
        #So I am going to need to iterate through the array.
        #Then I am going to need to iterate to the right -So potentially a second loop.
            #In this iteration, goal is to find the greatest element to its right so not including current index position.
        
        #I could create an array that I store the values in.
            #From there, make sure to change the last index to -1.
            #I could use the length -1 in order to get the last index of the array and update it to -1
            #Finally return the newely created and adjusted array.

        new_array = [0] * len(arr)
        #Starting Position
        for i in range(len(arr)):
            #Postion infront of starting position
            biggest_val = -1    
            for j in range(i+1, len(arr)):
                #Need to go down the list soooo.
                biggest_val = max(arr[j], biggest_val)
            new_array[i] = biggest_val
        return new_array
