# Longest Consecutive Sequence (Medium)

> **AI Assistance Disclosure:** This document was generated with the help of Claude (Anthropic). AI was used to provide hints, identify bugs, and guide problem-solving — **not** to provide the final solution. All code attempts were written by me, with AI providing feedback and direction.

**LeetCode Problem:** [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

---

## Problem Summary

Given an unsorted array of integers `nums`, return the length of the longest consecutive sequence of elements. Must run in O(n) time.

---

## How AI Assisted

| Area | How AI Assisted |
|---|---|
| **Core insight** | Guided toward the key idea: a number is the start of a sequence only if `num - 1` doesn't exist in the collection |
| **Data structure selection** | Steered away from dictionary, list, and tuple toward using a **set** for O(1) membership checks |
| **Algorithm structure** | Suggested using a **while loop** to extend from each sequence start, rather than relying on set iteration order |
| **Bug identification** | Caught a variable name typo (`nums` vs `num` in the for loop) |
| **Minor simplification** | Suggested tracking a single `longest` variable instead of building a `counts` list |
| **Documentation** | Compiled all guidance into this markdown file |

---

## Key Concepts Learned

### 1. Identifying Sequence Starts

A number is the **start** of a consecutive sequence if `num - 1` is NOT in the set. This avoids redundant work — you only start counting from the true beginning of each sequence.

### 2. Why a Set?

- **List/Tuple:** O(n) lookup — checking `if x in list` scans the whole thing
- **Dictionary:** Works but overkill — you don't need key-value pairs
- **Set:** O(1) lookup, automatically removes duplicates, perfect for existence checks

### 3. Using a While Loop to Extend Sequences

Since set iteration order is arbitrary, you can't rely on a running counter across iterations. Instead, once you find a sequence start, use a while loop to walk forward (`num + 1`, `num + 2`, ...) until the chain breaks.

### 4. Time Complexity: Still O(n)

Even though there's a loop inside a loop, each number is only visited a constant number of times across the entire run — the while loop only fires from sequence starts.

---

## Bug Caught

### Variable Name Typo
```python
# Bug: using 'nums' in loop but 'num' inside
for nums in numset:
    if num - 1 not in numset:  # 'num' is undefined!

# Fix:
for num in numset:
    if num - 1 not in numset:
```

---

## Final Approach

1. Convert `nums` to a `set` for O(1) lookups and deduplication
2. For each number, check if it's a sequence start (`num - 1 not in num_set`)
3. If it is, use a while loop to count how far the sequence extends
4. Track the longest sequence found

---

## Time & Space Complexity

- **Time:** O(n) — each element visited at most twice
- **Space:** O(n) — storing the set
