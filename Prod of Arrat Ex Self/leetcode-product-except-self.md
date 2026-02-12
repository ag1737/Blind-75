# Products of Array Except Self (Medium)

## Problem
Given an integer array `nums`, return an array `output` where `output[i]` is the product of all elements except `nums[i]`.

**Follow-up:** Solve in O(n) without division.

---

## Approach Evolution

### Attempt 1 — Remove & Reinsert
**Idea:** For each element, remove it from `nums`, multiply the rest, append to result, then add it back.

```python
for i in nums:
    nums.remove(i)
    for j in nums:
        startingnum = startingnum * j
    finalres.append(startingnum)
    nums.append(i)
    startingnum = 1
```

**Issues identified:**
- Initially forgot to reset `startingnum` and had a variable assignment bug (`result` vs `startingnum`) — fixed quickly
- `append` puts the removed element at the **end**, changing list order
- `remove` takes the **first occurrence**, so with a shifted list the wrong element gets removed
- Mutating a list while iterating over it causes unpredictable behaviour

### Attempt 2 — Skip by Value
**Idea:** Instead of mutating the list, skip the current element using a condition.

```python
for i in nums:
    for j in nums:
        if j != i:
            startingnum = startingnum * j
        else:
            startingnum * 1
```

**Issue identified:**
- Comparing **values** not **positions** — breaks with duplicates
- e.g. `nums = [0, 0]`: every `0` gets skipped, result is just `1 * 1` instead of `0`

### Attempt 3 — Enumerate (In Progress)
**Idea:** Use `enumerate` to compare by **index** rather than value, correctly skipping only the current position.

```python
for i, v in enumerate(nums):
    for j, w in enumerate(nums):
        if j != i:
            startingnum = startingnum * w
```

**Status:** Implementing and testing.

---

## Key Lessons
- **Don't mutate a list while iterating over it** — leads to skipped elements and unpredictable behaviour
- **Value comparison vs index comparison** — when elements can be duplicates, always use index to identify position
- `enumerate()` returns **(index, value)** — index first, value second
- `list.remove(x)` removes the **first occurrence** of value `x`, not a specific position
- `list.append(x)` adds to the **end**, not the original position

---

## Complexity (Current Approach)
- **Time:** O(n²) — nested loop
- **Space:** O(n) — result array
- **Follow-up challenge:** O(n) solution without division still to explore
