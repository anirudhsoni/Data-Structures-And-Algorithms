class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast,slow=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2=0
        while slow2!=slow:
            slow2=nums[slow2]
            slow=nums[slow]
        return slow

        



'''
Use Floyd's algo.
'''