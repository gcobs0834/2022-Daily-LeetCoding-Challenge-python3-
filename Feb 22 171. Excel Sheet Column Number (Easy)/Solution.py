# From Right to Left O(N) | O(1)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res, carry = 0, 0
        for s in columnTitle[::-1]:
            res += (ord(s) - ord('A') + 1) * (26 ** carry)
            # print("Letter: {} COL Num: {} Times {} Res = {}".format(s, ord(s) - ord('A') + 1, 26**carry, res))
            carry += 1
        return res
# Left to Righ O(N) | O(1)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for s in columnTitle:
            res *= 26
            res += ord(s) - ord('A') + 1
        return res
