# Two Pointer & Valid Palindrome - Study Notes

## Two Pointer Technique

Two pointers use two indices to traverse a data structure (usually a sorted array), reducing O(n²) brute force solutions down to O(n).

### Two Main Patterns

**1. Converging pointers** — One at the start, one at the end, moving inward based on a condition. Works because sorted order means moving a pointer has a predictable effect (e.g. increasing or decreasing a sum). Examples: Two Sum II, Container With Most Water, Valid Palindrome.

**2. Same-direction (fast/slow)** — Both move forward but at different speeds or under different conditions. The slow pointer tracks where to place the next valid element while the fast one scans ahead. Examples: Remove Duplicates.

### Why It Works

Requires **monotonic structure** (usually a sorted array) so moving a pointer has a predictable outcome. This lets you make a greedy decision at each step, eliminating large chunks of the search space — turning O(n²) into O(n).

---

## Valid Palindrome - Naive Solution Bug

[LeetCode 125 - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

`reversed()` returns an **iterator**, not a string, so comparing it directly to a string always returns `False`.

```python
# Bug
return s2 == reversed(s2)  # always False

# Fix — use slicing
return s2 == s2[::-1]

# Or wrap reversed in join
return s2 == ''.join(reversed(s2))
```
