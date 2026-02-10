# Top K Frequent Elements - Notes & Hints

**LeetCode Difficulty:** Medium

## Problem Summary

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements within the array.

## My Approach

1. Create a `defaultdict(int)` called `count` to build a frequency map of all elements — O(n)
2. Sort the dictionary by values in descending order so the most frequent elements come first
3. Extract the keys into a list and return the first `k` elements

## Hints & Lessons Learned

### Building the Frequency Map

Using `defaultdict(int)` is clean and efficient. Loop through `nums` and increment the count for each element. This step is O(n).

### Sorting a Dictionary by Value

- Use `sorted()` with a `key` parameter to sort by dictionary values
- Use `reverse=True` or `reversed()` to sort in **descending** order so the most frequent elements come first

### Bug: Wrapping `.keys()` in Square Brackets

- `[dict.keys()]` creates a list containing **one item** — the `dict_keys` object itself
- `list(dict.keys())` correctly unpacks the keys into individual elements in a list

### Bug: Slicing for the First K Elements

- `list[index:]` returns everything from `index` **onwards** (i.e. to the end)
- `list[:k]` returns the **first k elements**, which is what we want here

### Complexity Consideration

- This approach runs in **O(n log n)** due to the sort step
- A more optimal O(n log k) solution exists using a **heap** — worth exploring after getting this version working

## Resources

- [Python - Sort Dictionaries by Key or Value (GeeksforGeeks)](https://www.geeksforgeeks.org/python/python-sort-python-dictionaries-by-key-or-value/)
- https://leetcode.com/problems/top-k-frequent-elements/
