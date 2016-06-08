"""
Given two arrays, write a function to compute their intersection.

- Each element in the result must be unique.
- The result can be in any order.
"""

def intersection(nums1, nums2):
        result = set()
        for elem in nums1:
            if elem in nums2:
                result.add(elem)
        return list(result)