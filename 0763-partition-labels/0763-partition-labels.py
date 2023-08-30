class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        l, r = 0, 0

        ans = []
        for i, c in enumerate(s):

            r = max(r,last[c])

            if i == r:
                ans += [r-l + 1]
                l = i+1

        return ans