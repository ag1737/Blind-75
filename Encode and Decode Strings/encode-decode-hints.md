# Encode and Decode Strings (LeetCode - Medium)

leetcode link is paywalled, here is the neetcode version: https://neetcode.io/problems/string-encode-and-decode/question

> **AI Assistance Disclosure:** This document was generated with the help of Claude (Anthropic). AI was used to provide hints, identify bugs, and guide problem-solving — **not** to provide the final solution. All code attempts were written by me, with AI providing feedback and direction.

---

## How AI Was Used

| Area | How AI Assisted |
|---|---|
| **Problem-solving direction** | Provided conceptual hints about delimiter strategies and length-prefixing without giving the solution |
| **Bug identification** | Identified a misuse of Python's `str.join()` method in my code |
| **Edge case awareness** | Pointed out trailing delimiter issues and delimiter fragility when input strings contain the delimiter character |
| **Algorithm guidance** | Suggested the length-prefixing approach as a robust alternative to character-based delimiters, with a format example |
| **Documentation** | Compiled all guidance into this markdown file |

---

## Hint 1: Understanding the Core Challenge

If you just join strings with a delimiter (like a comma), what happens if one of the original strings *contains* that delimiter? You'd split incorrectly on decode.

**Key question:** How can you encode the string so that the decoder knows *exactly* where each original string starts and ends, regardless of what characters are in the strings?

**Hint:** Think about how real-world protocols (like HTTP) solve a similar problem. When a server sends you a message body, how does it tell you where the body ends? It doesn't rely on a special character — it tells you the *length* upfront.

---

## Hint 2: Bug Fix — `str.join()` Behaviour

My original code:

```python
stringcoded.join(i + "∫")
```

**Issue:** `str.join()` uses the string it's called on as a separator *between* items of an iterable. So this inserts `stringcoded` between each *character* of `i + "∫"`, and the result isn't assigned back to anything.

**Fix:** Use `+=` for simple string concatenation.

---

## Hint 3: Trailing Delimiter Produces Extra Empty String

If you append a delimiter after *every* string (including the last one), then `split()` gives an extra empty string at the end.

Example: `["Hello","World"]` → `"Hello∫World∫"` → split gives `["Hello", "World", ""]`

**Fix:** Slice off the trailing delimiter with `[:-1]`, or don't append it after the last string.

---

## Hint 4: Delimiter Fragility — The Real Problem

Using any special character as a delimiter is fragile. If one of the input strings contains that character, decode breaks.

Example with `∫` as delimiter:

- Input: `["Hello∫World", "Test"]`
- Encode produces: `"Hello∫World∫Test"`
- Decode splits on every `∫` and gives: `["Hello", "World", "Test"]` — **three strings instead of two**

No matter what character you pick, the input could contain it. This is the key insight the problem is testing.

---

## Hint 5: The Robust Approach — Length-Prefixing

For each string, store its length and then the string itself. The decoder reads the length, knows exactly how many characters to grab, and doesn't care about any characters inside the string.

Use a small, fixed separator between the length number and the content so the decoder knows where the length ends and the string begins.

Example format: `5#Hello5#World`

- Read `5`, skip `#`, grab 5 characters → `"Hello"`
- Read `5`, skip `#`, grab 5 characters → `"World"`

This works regardless of what characters appear in the strings.

---

## My Code Iterations

### Attempt 1 — `join()` bug and trailing delimiter issue

```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        stringcoded = ""
        for i in strs:
            stringcoded.join(i + "∫")  # Bug: join misuse
        return stringcoded

    def decode(self, s: str) -> List[str]:
        decodedlist = s.split("∫")  # Issue: extra empty string
        return decodedlist
```

### Attempt 2 — Fixed bugs, but still vulnerable to delimiter collision

```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        stringcoded = ""
        for i in strs:
            stringcoded += i + "∫"
        return stringcoded[:-1]

    def decode(self, s: str) -> List[str]:
        decodedlist = s.split("∫")
        return decodedlist
```

### Attempt 3 — TODO: Implement length-prefixing approach
