class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalres = []
        for i,v in enumerate(nums):
            startingnum = 1

            for j, k in enumerate(nums):
                if j != i :
                    startingnum = startingnum * k
                else:
                    startingnum * 1
            finalres.append(startingnum) 
        return finalres
