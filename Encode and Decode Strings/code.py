class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
           DBS = "∫∫∫"
           return DBS 
        stringcoded = ""
        for i in strs:
            stringcoded += i + "∫"
        return stringcoded[:-1]

    def decode(self, s: str) -> List[str]:
        if s == "∫∫∫":
            return []
        decodedlist = s.split("∫")
        return decodedlist
