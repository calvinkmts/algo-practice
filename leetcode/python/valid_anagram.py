class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        ss = sorted([c for c in s])  # ss meaning like array of s
        ts = sorted([c for c in t])

        for i in range(len(s)):
            if ss[i] != ts[i]:
                return False

        return True