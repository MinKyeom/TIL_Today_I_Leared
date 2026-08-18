"""
출처: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n= len(nums2)
        if (m+n)%2==0:
            All = nums1+nums2
            All.sort()
            medium = (m+n)//2
            return (All[medium-1]+All[medium])/2
        else:
            All =nums1+nums2
            All.sort()
            medium = (m+n)//2
            return All[medium]