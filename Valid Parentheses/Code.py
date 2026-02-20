class Solution:
    def isValid(self, s: str) -> bool:
      #creating a stack and map for parenthesis
        bracketlist = []
        BracketMap = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for i in s:
          #if bracket is a opening bracket
            if i in BracketMap.keys():
                bracketlist.append(i)
              #if bracket is a closing bracket and we have seen an opening bracket
            elif i in BracketMap.values() and len(bracketlist) != 0:
                a = bracketlist[-1]
              #if the closing bracket matches the last opening bracket visited and then remove the compliment opening bracket from list of opening brackets visited
                if BracketMap[a] == i:
                    bracketlist.pop()
                else:
                  #mismatch in brackets
                    return False
            else:
              #no brackets forund or closing bracket with opening brackets
                return False
        
#if all the opening brackets have found a match return True 
        if len(bracketlist) == 0:
            return True
        return False
