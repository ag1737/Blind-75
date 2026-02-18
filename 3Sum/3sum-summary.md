# 3Sum - Problem Summary

## Approach
- Sort the array first
- Fix `i` using `for i in range(len(nums))` and use two pointers (`Lpointer`, `Rpointer`) to find pairs that sum to `-nums[i]`
- `Lpointer` starts at `i + 1`, `Rpointer` starts at `len(nums) - 1`
- If sum too small → move `Lpointer` right
- If sum too big → move `Rpointer` left
- If sum == 0 → add triplet, move both pointers inward

## Duplicate Handling
- **For `i`**: Skip if `i > 0 and nums[i] == nums[i-1]` — avoids reprocessing the same fixed value
- **For `Lpointer`/`Rpointer`**: Only skip duplicates *inside the `else` block*, after finding a valid triplet — avoids adding the same triplet again

## Key Insight
Sorting allows duplicate detection via simple adjacent comparisons rather than needing a hashmap or set.

---

## Problem Link
[LeetCode 15 - 3Sum](https://leetcode.com/problems/3sum/)

## Notes
> ⚠️ **I used AI heavily for this question — needs revisiting independently.**
>
> I looked at the LeetCode solution and was most confused by:
> - The duplicate skipping logic for `i`
> - The duplicate skipping logic for the two pointers
>
> Come back to this and try to solve it from scratch without assistance.
