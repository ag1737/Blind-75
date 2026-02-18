class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            Lpointer = i + 1
            Rpointer = len(nums) - 1
            
            while Lpointer < Rpointer:
                if nums[i] + nums[Lpointer] + nums[Rpointer] > 0:
                    Rpointer -= 1
                elif nums[i] + nums[Lpointer] + nums[Rpointer] < 0:
                    Lpointer += 1
                else:
                    res.append([nums[i], nums[Lpointer], nums[Rpointer]])
                    Lpointer += 1
                    Rpointer -= 1
                    while Lpointer < Rpointer and nums[Lpointer] == nums[Lpointer-1]:
                        Lpointer += 1
                    while Lpointer < Rpointer and nums[Rpointer] == nums[Rpointer+1]:
                        Rpointer -= 1
        
        return res
