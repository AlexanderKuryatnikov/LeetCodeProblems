from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: no palindrome': [
        '1234',
        '1'
    ],
    '2: single char': [
        'a',
        'a'
    ],
    '3: palindrome exists': [
        'babad',
        'bab'
    ]
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.longestPalindrome(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
