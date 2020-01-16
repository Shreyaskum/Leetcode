class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        out = []
        bool = False
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                            out.append(nums[i])
                            out.append(nums[j])
                            out.append(nums[k])
                            z = out
                            for x in res:
                                if ((z[0] in x and x[1] in out and x[2] in out)):
                                   
                                    bool = True
                            if bool == False:
                                res.append(out) 
                            out = []
                            bool = False
                            

        return res


            
                
            
            