class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        nums.sort()

        i, n = 0, len(nums)

        while i < n :

            target = -nums[i]
            j, k = i + 1, n - 1

            while j < k:
                
                currSum = nums[j] + nums[k]
                
                if currSum == target:
                    ans.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif currSum > target: k -= 1
                else: j += 1

            i += 1

        return list(ans)