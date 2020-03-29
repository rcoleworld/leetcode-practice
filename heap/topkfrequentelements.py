"""
347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.
"""
import collections
import heapq

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = collections.Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)