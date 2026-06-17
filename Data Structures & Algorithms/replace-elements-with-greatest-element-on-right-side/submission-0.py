class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # #For replacing every elemint in the array with the greatest elements among the elements to its right part,
        #     # I am going to be iterating through the array.
        #     # I am going to see what the greatest element is from the right.
        #         #Once I reach the end of the list, I will replace the index with the greatest element.

        # #The last element in the list I could just get the length minus 1 to get the last index and set it to -1
        # greatest_element = 0
        # array_len = len(arr)
        # for num in range(array_len):
        #     for j in range(num+1):
        #         greatest_element = max(arr[num], num[j])
        #     arr[num] = greatest_element

        n = len(arr)
        ans = [0] * n
        for i in range(n):
            rightMax = -1
            for j in range(i +1, n):
                rightMax = max(rightMax, arr[j])
            ans[i] = rightMax
        return ans