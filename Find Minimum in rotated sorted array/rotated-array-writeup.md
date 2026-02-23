# Find Minimum in Rotated Sorted Array

**Problem:** [LeetCode 153 - Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## AI-Assisted Development Log

This document tracks how my solution evolved through iterative problem-solving with AI (Claude) as a guide. Claude provided no hints or solutions upfront — only feedback on bugs, edge cases, and nudges toward better approaches.

---

## Attempt 1 — Linear Scan from Midpoint

My first instinct was to start at the midpoint and walk outward in both directions, checking neighbours to find where the rotation happened.

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        midpoint = len(nums) - 1 // 2
        left = midpoint - 1
        right = midpoint + 1
        while right < len(nums) - 1:
            if nums[right] > midppoint and nums[midpoint] < nums[left]:
                return nums[midpoint]
            elif nums[midpoint] < nums[right]:
                midpoint += 1
                right = midpoint + 1
                left = midpoint - 1
            else:
                return nums[right]
        midpoint = len(nums) - 1 // 2
        left = midpoint - 1
        right = midpoint + 1
        while left > 0:
            if nums[midpoint] < nums[left]:
                return nums[midpoint]
            elif nums[midpoint] > nums[left]:
                midpoint -= 1
                left = midpoint - 1
                right = midpoint + 1
            else:
                return nums[left]
```

**AI Feedback:**
- Operator precedence bug: `len(nums) - 1 // 2` evaluates as `len(nums) - 0` due to `//` binding tighter than `-`.
- Typo: `midppoint` → `midpoint`.
- Nudge: think about time complexity — stepping one index at a time is O(n), not O(log n).

---

## Attempt 2 — Recognising the Binary Search Insight

After the complexity nudge, I realised I could jump to the midpoint and compare against the ends to determine which half contains the minimum, eliminating half the array each time.

> "I can go to the midpoint immediately and if nums left is bigger than nums midpoint then I have my answer. Then I can go to the end and if nums end is less than nums midpoint then I know it's in the right side."

---

## Attempt 3 — Array Slicing Approach

I translated that insight into code using array slicing:

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        midpoint = (len(nums) - 1) // 2
        right = len(nums) - 1
        left = 0
        while len(nums) > 1:
            if nums[midpoint] > nums[right]:
                nums = nums[midpoint:]
                midpoint = (len(nums) - 1) // 2
                right = len(nums) - 1
            elif nums[midpoint] < nums[right]:
                nums = nums[:midpoint]
                midpoint = (len(nums) - 1) // 2
                right = len(nums) - 1
        return nums[0]
```

**AI Feedback:**
- Slicing is O(n) per iteration, undermining the O(log n) goal.
- `nums[:midpoint]` excludes the midpoint, which could be the minimum itself — traced through `[3, 4, 5, 1, 2]` to demonstrate.
- Suggestion: use pointer movement instead of slicing.

---

## Attempt 4 — Pointer-Based with Neighbour Check

Switched to the standard binary search structure with left/right pointers, but added an unnecessary neighbour check:

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        while left < right:
            midpoint = (left + right) // 2
            if nums[midpoint - 1] < nums[midpoint] and nums[midpoint] < nums[midpoint + 1]:
                return nums[midpoint]
            elif nums[midpoint] > nums[right]:
                left = midpoint
            else:
                right = midpoint
        return num[midpoint]
```

**AI Feedback:**
- `left = midpoint` causes infinite loops (e.g. `left=3, right=4`). Need `left = midpoint + 1`.
- Neighbour check risks index out of bounds and isn't needed — the loop converges naturally.
- Typo: `num` → `nums`, and should return `nums[left]` since `midpoint` may be stale.

---

## Attempt 5 — Clean Binary Search (Near-Final)

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        while left < right:
            midpoint = (left + right) // 2
            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint - 1
        return nums[midpoint]
```

**AI Feedback:**
- `right = midpoint - 1` can skip the minimum — midpoint could be the answer, so use `right = midpoint`.
- Return `nums[left]` instead of `nums[midpoint]`.

---

## Final Solution

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        while left < right:
            midpoint = (left + right) // 2
            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint
        return nums[left]
```

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

---

## Key Takeaways

1. **Operator precedence matters** — `len(nums) - 1 // 2` vs `(len(nums) - 1) // 2` is a subtle but critical difference.
2. **Binary search is about eliminating halves** — my first instinct was a linear scan from the middle. The key insight was comparing `nums[midpoint]` to `nums[right]` to decide which half to discard.
3. **Pointer movement vs slicing** — slicing creates new arrays and defeats the purpose of O(log n). Moving pointers keeps it efficient.
4. **Off-by-one decisions are the hardest part** — `left = midpoint + 1` vs `left = midpoint` and `right = midpoint` vs `right = midpoint - 1` depend on whether the midpoint can be the answer. This was the last thing to click.
5. **Return the right variable** — after the loop, `left == right` is your answer; `midpoint` may be stale from a previous iteration.
