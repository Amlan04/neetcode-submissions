class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = 0
        m = len(numbers)-1
        while n<m:
            if numbers[n] + numbers[m] == target:
                return [n+1,m+1]
            elif numbers[n] + numbers[m] > target:
                m -= 1
            else :
                n += 1
        