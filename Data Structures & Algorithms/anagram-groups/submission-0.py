class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap={}

        def freqmap(string):
            keys=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            sp_strmap = dict.fromkeys(keys,0)
            for i in string:
                for j in sp_strmap:
                    if i==j:
                        sp_strmap[j]+=1
            mapvalues=[]
            for K in sp_strmap:
                mapvalues.append(sp_strmap[K])
            mapvalues_tup=tuple(mapvalues)
            return mapvalues_tup
        for i in strs:
            key = freqmap(i)
            if key not in hashmap:
                hashmap[key]=[i]
            elif key in hashmap:
                hashmap[key].append(i)
        return list(hashmap.values())