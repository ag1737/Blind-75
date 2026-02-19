class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #create a left and right pointer starting at the start and end respectively
        L = 0
        R = len(heights) - 1
        #max area variable
        MA = 0 

        while L < R:
            #find the current min height
            currentheight = min(heights[L], heights[R])
            #find the current area
            currentArea = (R-L) * currentheight
            #if the current area is bigger than the max are update it
            if currentArea > MA:
                MA = currentArea
            #move the pointer at the smaller array closer
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return MA
