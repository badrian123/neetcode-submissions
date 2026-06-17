class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 0
        list_of_products = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != p:
                    product = product * nums[j]
            list_of_products.append(product)
            p += 1
        return list_of_products