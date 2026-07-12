class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        L1=[]
        for i in nums:
            if i not in L1:
                L1.append(i)
            elif i in L1:
                return True
                break
        else:
            return False