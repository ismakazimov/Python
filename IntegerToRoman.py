class Solution:
    def int_to_Roman(self, num: int) -> str:
        num_sym = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
                   ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],
                   ["D", 500], ["CM", 900], ["M", 1000]]

        results = ""
        for sym, val in reversed(num_sym):
            if num // val:
                count = num // val
                results = results + (sym * count)
                num = num % val
        return results

solution = Solution()

result = solution.int_to_Roman(1998)
print(result)
