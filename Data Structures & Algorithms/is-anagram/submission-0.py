class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        keys=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        hashmap=dict.fromkeys(keys,0)
        hashmap2=dict.fromkeys(keys,0)
        for I in s:
            for J in hashmap:
                if I==J:
                    hashmap[J]+=1
        for X in t:
            for Y in hashmap2:
                if X==Y:
                    hashmap2[Y]+=1
        if hashmap==hashmap2:
            return True
        else:
            return False
        