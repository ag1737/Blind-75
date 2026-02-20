# Valid Parentheses - LeetCode #20

**Link:** [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)  
**Difficulty:** Easy  
**Topic:** Stack, String  
**Date:** 20 February 2026

---

## Problem Summary

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. An input string is valid if open brackets are closed by the same type of brackets and in the correct order.

---

## My Approach

### First Attempt (Incorrect)
Initially planned to separate the string into an open brackets list and a closed brackets list, reverse the closed list, and use a dictionary mapping to compare them. This failed on inputs like `"([)]"` because it only checked counts, not ordering or nesting.

### Final Approach — Stack
Used a stack (`bracketlist`) and a dictionary mapping open brackets to their corresponding closing brackets.

- For every character in the string, if it's an open bracket, push it onto the stack.
- If it's a closing bracket and the stack is non-empty, check if it matches the top of the stack. If it does, pop. If not, return `False`.
- If it's a closing bracket and the stack is empty, return `False` immediately.
- After the loop, if the stack is empty, return `True`.

---

## Final Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        bracketlist = []
        BracketMap = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for i in s:
            if i in BracketMap.keys():
                bracketlist.append(i)
            elif i in BracketMap.values() and len(bracketlist) != 0:
                a = bracketlist[-1]
                if BracketMap[a] == i:
                    bracketlist.pop()
                else:
                    return False
            else:
                return False

        if len(bracketlist) == 0:
            return True
        return False
```

---

## Complexity

| | Complexity |
|---|---|
| Time | O(n) — single pass through the string |
| Space | O(n) — stack grows at most to length of input |

---

## Edge Cases Considered

| Input | Expected | Reason |
|---|---|---|
| `"()"` | `True` | Basic match |
| `"()[]{}"` | `True` | Multiple types, correct order |
| `"([)]"` | `False` | Wrong nesting order |
| `"]"` | `False` | Closing bracket with empty stack |

---

## Key Learnings

- A **stack** naturally handles last-in-first-out bracket matching.
- Separating brackets into two lists and comparing them loses ordering information.
- When encountering a closing bracket with an empty stack, return `False` immediately — don't wait until the end.
- Multiple lists that all scale with input size `n` have a combined space complexity of O(n), not O(n * m).

---

## Where I Used AI

I completed this problem in a simulated FAANG interview format with Claude. The code was written entirely by me without hints or solutions. Claude acted as an interviewer — asking me to trace through edge cases, stress testing my approach with tricky inputs, and prompting me to identify bugs in my own code. Claude also discussed time and space complexity with me after I arrived at my final solution.
