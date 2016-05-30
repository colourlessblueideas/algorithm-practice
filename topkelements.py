"""
Given a non-empty array of integers, return the k most frequent elements.
Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

def topKFrequent(nums, k):
        counts = {}
        for num in nums:
            if counts.has_key(num):
                counts[num] += 1
            else:
                counts[num] = 1
        
        sort_counts = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
        return [i[0] for i in sort_counts][:k]