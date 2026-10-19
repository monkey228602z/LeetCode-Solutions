class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        f = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return f
            f += first[i]
            
        return f
