class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        counts = [] 
        count = 0 
        for num in numset:
            if num - 1 not in numset:
                while num + 1 in numset:
                    count += 1
                    num += 1 
                count +=1
                counts.append(count)
                count = 0 
        if len(counts) == 0 :
            counts = [0]
        return max(counts)
