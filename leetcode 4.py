class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst=[]
        dic={}
        for a in strs:
            key=''.join(sorted(a))
            if key in dic:
                dic[key] = dic[key] + [a]
            else:
                dic[key]=[a]
        for value in dic.values():
            lst.append(value)
        return lst