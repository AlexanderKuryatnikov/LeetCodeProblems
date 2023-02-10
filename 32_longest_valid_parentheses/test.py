from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: starts with excessive opening': [
        '(()',
        2
    ],
    '2: starts with excessive closing bracket': [
        ')()()',
        4
    ],
    '3: empty string': [
        '',
        0
    ],
    '4: opening brackets only': [
        '((((',
        0
    ],
    '5: closing brackets only': [
        ')))))))',
        0
    ],
    '6: opening braket': [
        '(',
        0
    ],
    '7: closing braket': [
        ')',
        0
    ],
    '8: excessive opening in the middle': [
        '(())()(()',
        6
    ],
    '9: excessive closing in the middle': [
        '(())())()',
        6
    ],
    '10: wrong order in the middle': [
        '()())((()())',
        6
    ],
    '11: valid brackets': [
        '((()))()(())',
        12
    ],
    '12: ends with excessive opening bracket': [
        '()(',
        2
    ],
    '12: ends with excessive closing bracket': [
        '())',
        2
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.longestValidParentheses(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
