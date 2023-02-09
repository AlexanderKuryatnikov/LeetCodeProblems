from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: n = 1': [
        1,
        ['()']
    ],
    '2: n = 3': [
        3,
        [
            '((()))',
            '(()())',
            '(())()',
            '()(())',
            '()()()'
        ]
    ]
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.generateParenthesis(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
