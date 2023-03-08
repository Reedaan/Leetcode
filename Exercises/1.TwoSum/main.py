nums = [3,2,3]
target = 6
        
class Solution:
    def twoSum(nums, target):
        for a in range(len(nums)- 1):
            test = target - nums[a]
            if test in nums:
                number_1 = a
                number_2 = nums.index(test)
                print(number_1, number_2)
            break
                
            
            
Solution.twoSum(nums, target)
