class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Setting the arrays to variables
        A, B = nums1, nums2
        #Adding up the lengths together
        total = len(nums1) + len(nums2)
        #Finding out what is half of the combined arrays.
        half = total // 2

        #Checking to see which array is bigger.
        #We want smaller array to be variable A
        if len(B) < len(A):
            A,B = B, A
        
        #Now the binary search part begins here.
        l, r = 0, len(A)-1
        while True:
            #This would be middle but it is set to i, i guess.
            i = (l+r)//2
            #This is half of the combined arrays minus half of array A and minus 2. I wonder why?
            j = half - i - 2

            #This part I don't understand and is where I get confused.
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i +1] if (i + 1) < len(A) else float("infinity")

            #Now this is done too for the second array. I don't understand here too.
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            #I don't understand this part too. So I guess the answer is returned on here.
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                     return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            #this is interesting in how the right pointer is moved on this elif 
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1