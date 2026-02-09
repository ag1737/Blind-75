class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      #create a dictionary
        HM = defaultdict(list)
        emptylist = []
        for i in strs:
          #for each word in the list, append the word if the sorted word exists in the hashmap, if not create a new key
            sortedstring = "".join(sorted(i))
            HM[sortedstring].append(i)
        #format for return, looking at the solution i realise that I can just use return list(HM.values())
        for i in HM.values():
            emptylist.append(i)
        
        return emptylist
