"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time.
"""

def majorityElement(nums):
        counts = dict()
        result = []
        for num in nums:
            if counts.has_key(num):
                counts[num] += 1
            else:
                counts[num] = 1
        n = len(nums)
        for key, val in counts.items():
            if val > int(n / 3):
                result.append(key)
        return result