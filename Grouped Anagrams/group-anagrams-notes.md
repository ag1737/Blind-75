# Group Anagrams - Learning Notes

## Specific Help Received

### 1. Algorithm Validation
- Confirmed that using sorted strings as hashmap keys is the correct approach
- Walked through the logic: first occurrence creates new list, subsequent occurrences append to existing list

### 2. Introduction to defaultdict
- Suggested using `defaultdict(list)` from the `collections` module
- Explained that it automatically creates empty lists for new keys, eliminating need for manual checks

### 3. Dictionary Methods Clarification
- Taught `.values()` method to extract all values from a dictionary
- Explained `.keys()`, `.values()`, and `.items()` for different iteration needs
- Clarified that `for key in dict` iterates over keys by default

### 4. Dictionary Iteration Patterns
- Explained why `for i, j in my_dict` doesn't work (tries to unpack the key string)
- Showed how to use `for key, value in my_dict.items()` for key-value pairs

### 5. Code Review and Bug Identification
When reviewing my code, identified these issues:
- Using `=` instead of `.append()` - overwrites the list instead of adding to it
- Using `HM.add(i)` - dictionaries don't have an `.add()` method
- Unnecessary `if sorted(i) in HM` check when using defaultdict
- Calling `sorted(i)` multiple times - should store in a variable

### 6. In-depth defaultdict Explanation
- Detailed walkthrough of how defaultdict differs from regular dictionaries
- Explained the "factory function" concept (passing `list` to create empty lists automatically)
- Showed step-by-step what happens when accessing a non-existent key

### 7. Important Clarification
- Emphasized that `sorted()` returns a list of characters, which needs to be joined into a string for use as a dictionary key

## Problem
Given an array of strings, group all anagrams together into sublists.

**Example:**
```
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

## Solution Approach

### Key Insight
Anagrams contain the same characters, so when sorted, they produce identical strings.
- "act" sorted → "act"
- "cat" sorted → "act"
- Both map to the same key!

### Algorithm
1. Use a hashmap where:
   - **Key** = sorted version of the word (e.g., "act")
   - **Value** = list of original words that match that sorted pattern

2. For each word in input:
   - Sort the word to get the key
   - Add the original word to the list at that key

3. Return all the values (the grouped lists)

## Python Implementation Strategy

### Using defaultdict
```python
from collections import defaultdict

# Create defaultdict with list as the default factory
HM = defaultdict(list)

# For each word
for word in strs:
    sorted_word = sorted(word)  # Returns a list of chars
    key = ''.join(sorted_word)  # Convert to string for the key
    HM[key].append(word)  # Automatically creates empty list if key doesn't exist

# Return all grouped lists
return list(HM.values())
```

### How defaultdict Works
- `defaultdict(list)` means: "when accessing a non-existent key, automatically create an empty list"
- No need for `if key in dict` checks!
- First access: creates `[]`, then appends
- Subsequent access: just appends to existing list

**Regular dict:**
```python
regular_dict["new_key"].append(value)  # KeyError!
```

**defaultdict:**
```python
default_dict["new_key"].append(value)  # Works! Auto-creates []
```

## Common Pitfalls Addressed

### 1. Not converting sorted() result to string
```python
sorted("act")  # Returns ['a', 'c', 't'] - a list!
''.join(sorted("act"))  # Returns "act" - a string (good for dict key)
```

### 2. Using = instead of .append()
```python
HM[key] = word  # Wrong! Overwrites the list
HM[key].append(word)  # Correct! Adds to the list
```

### 3. Trying to use .add() on a dictionary
```python
HM.add(word)  # Wrong! Dicts don't have .add()
```

### 4. Manually checking if key exists with defaultdict
```python
# Unnecessary with defaultdict:
if key in HM:
    HM[key].append(word)
else:
    HM[key] = [word]

# Just do this:
HM[key].append(word)
```

## Dictionary Methods Reference

- `.keys()` - iterate over keys only
- `.values()` - iterate over values only  
- `.items()` - iterate over (key, value) pairs

```python
for key, value in my_dict.items():
    print(key, value)
```

## Time Complexity
- Sorting each word: O(k log k) where k is length of word
- n words: O(n * k log k)
- Overall: **O(n * k log k)**

## Space Complexity
- Storing all words in hashmap: **O(n * k)**

## Key Takeaways
1. Sorted strings make great keys for grouping anagrams
2. defaultdict eliminates need for existence checks
3. Always append to lists, don't reassign with =
4. Dictionary methods: .keys(), .values(), .items()
