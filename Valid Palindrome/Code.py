class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        right = len(s2) - 1
        res = True
        while left<right:
            if s2[left] == s2[right]:
                left += 1
                right -= 1
            else:
                return False

        return res
