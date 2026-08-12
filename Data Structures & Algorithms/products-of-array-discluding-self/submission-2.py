class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        pref, suff = [1 for i in range(lenght)],[1 for i in range(lenght)]
        pre, suf = 1,1
        for i in range(lenght):
            pre *= nums[i]
            pref[i] = pre
        for i in range(lenght-1, -1, -1):
            suf *= nums[i]
            suff[i] = suf
        
        res = [0]*lenght
        res[0] = suff[1]
        res[lenght-1] = pref[lenght-2]

        for i in range (1,lenght-1):
            res[i] = pref[i-1]*suff[i+1]
            
        return res   

        