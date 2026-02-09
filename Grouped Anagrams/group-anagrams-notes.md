# Group Anagrams - Learning Notes- USED AI TO CREATE .MD FILE

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
https://leetcode.com/problems/group-anagrams/description/
