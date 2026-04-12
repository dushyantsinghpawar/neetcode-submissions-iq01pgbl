class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        m, n = len(nums1), len(nums2)
        i = j = 0

        for count in range(m + n - 1):
            if i < m and j < n:
                if nums1[i] <= nums2[j]:
                    ans.append(nums1[i])
                    i += 1
                else:
                    ans.append(nums2[j])
                    j += 1
        if i < m:
            ans += nums1[i:]
        elif j < n:
            ans += nums2[j:]
        
        xm = (m + n) // 2
        if (m + n) % 2 == 0:
            return (ans[xm] + ans[xm - 1]) / 2
        else:
            return ans[xm]