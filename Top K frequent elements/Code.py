class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) 
        for i in nums:
            count[i] += 1
        sorteddictdesc ={k:v for k,v in reversed(sorted(count.items(), key=lambda item: item[1]))}
        listofnumbers = list(sorteddictdesc.keys())
        print(listofnumbers)
        index = k - 1
        return listofnumbers[:k]
