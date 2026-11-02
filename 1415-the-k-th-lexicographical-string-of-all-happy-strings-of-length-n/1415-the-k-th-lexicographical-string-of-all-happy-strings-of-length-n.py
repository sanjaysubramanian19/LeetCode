class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def backtrack(s):
            if len(s) == n:
                res.append(s)
                return

            for c in "abc":
                if not s or s[-1] != c:
                    backtrack(s + c)

        backtrack("")
        return res[k - 1] if k <= len(res) else ""