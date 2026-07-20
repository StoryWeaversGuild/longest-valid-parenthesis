# Longest Valid Parentheses

## Problem Statement

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.
Example 1:Input: s = "(()"Output: 2Explanation: The longest valid parentheses substring is "()".
Example 2:Input: s = ")()())"Output: 4Explanation: The longest valid parentheses substring is "()()".
Example 3:Input: s = ""Output: 0
Constraints:
0 <= s.length <= 3 * 104
s[i] is '(', or ')'

## Approach

This solution uses a stack to keep track of indices of opening parentheses. A sentinel value (-1) is initially pushed to handle edge cases efficiently. Whenever a matching pair is found, the length of the current valid substring is calculated and the maximum length is updated.

## Algorithm

1. Initialize a stack with `-1`.
2. Traverse the string.
3. Push the index of every `'('`.
4. For every `')'`, pop the stack.
5. If the stack becomes empty, push the current index.
6. Otherwise, calculate the length of the valid substring.
7. Return the maximum length found.

## Complexity

- Time Complexity: **O(n)**
- Space Complexity: **O(n)**

## Files

- `solution.py` - Python implementation.
- `test_cases.py` - Sample test cases.
- `requirements.txt` - No external dependencies.

## How to Run

```bash
python test_cases.py
```

## Sample Test Cases

| Input | Output |
|-------|--------|
| `(()` | `2` |
| `)()())` | `4` |
| `""` | `0` |
