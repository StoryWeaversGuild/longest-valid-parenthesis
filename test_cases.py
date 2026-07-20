from solution import Solution

sol = Solution()

test_cases = [
    ("(()", 2),
    (")()())", 4),
    ("", 0),
    ("()(()", 2),
    ("()(())", 6),
]

for s, expected in test_cases:
    result = sol.longestValidParentheses(s)
    print(f"Input: {s!r} | Expected: {expected} | Got: {result}")
