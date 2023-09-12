s1 = "delete"
s2 = "leet"
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1 = sorted(s1)
        s2 = sorted(s2)
        print(list(set(s1)^set(s2)))
        print(ord("d"))
s = Solution().minimumDeleteSum(s1,s2)