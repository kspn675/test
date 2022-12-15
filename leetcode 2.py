class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        single=set()
        for i in nums:
            if i in single:
                single.remove(i)
            else:
                single.add(i)
        return list(single)
                            
                                        
                                                    



            
            
            
        