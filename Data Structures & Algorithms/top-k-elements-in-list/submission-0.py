class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            elif i in hashmap:
                hashmap[i]+=1
        sortedhash=dict(sorted(hashmap.items(),key= lambda x : x[1], reverse=True))
        outputlist=[]
        keys = list(sortedhash.keys())
        for p in range(k):
            outputlist.append(keys[p])
        return outputlist