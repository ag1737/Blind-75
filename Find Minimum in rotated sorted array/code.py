class Solution:
    def findMin(self, nums: List[int]) -> int:
        #right is at the end of array left is at the start
        right = len(nums) - 1
        left = 0 
        
        while left < right:
        #check from middle if a smaller number is after the midpoint if so
        #means that minimum is on left side and we shorten search to one side of array
        #do opposite if no smaller number at the end of the array
            midpoint = (left + right) // 2
            #check right side
            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            #check left side 
            else:
                right = midpoint
        return nums[left]

