"""
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.
"""
import collections

def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Check character count of both strings
def isAnagram(self, s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)