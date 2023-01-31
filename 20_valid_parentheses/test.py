from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: row of brackets': [
        '()[]{}',
        True
    ],
    '2: single opening bracket': [
        '(',
        False
    ],
    '3: single closing bracket': [
        ')',
        False
    ],
    '4: intersecting brackets': [
        '([)]',
        False
    ],
    '5: nested brackets': [
        '(([({()})]))[{[]}]{{[()]}}',
        True
    ],
    '6: wrong order': [
        ')(',
        False
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.isValid(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
