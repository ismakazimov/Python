class Solution:
    def two_sum(self, numbers, target):
        prevMap = {}
        for indice, number in enumerate(numbers):
            differ = target - number
            if differ in prevMap:
                return [prevMap[differ], indice]
            prevMap[number] = indice
        return

solution = Solution()

nums = [2, 6, 11, 9]
target = 15

result = solution.two_sum(nums, target)
print(result)