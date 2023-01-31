from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: single row': [
        'abcd',
        1,
        'abcd'
    ],
    '2: leetcod example 1': [
        'PAYPALISHIRING',
        3,
        'PAHNAPLSIIGYIR'
    ],
    '3: leetcode example 2': [
        'PAYPALISHIRING',
        4,
        'PINALSIGYAHRPI'
    ],
    '4: index error': [
        'abcdefghijklmnop',
        5,
        'aibhjpcgkodflnem'
    ],
    '5: two rows 1': [
        'abcdefg',
        2,
        'acegbdf'
    ],
    '6: two rows 2': [
        'abcdefgh',
        2,
        'acegbdfh'
    ],
    '7: several rows with single char': [
        'a',
        3,
        'a'
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.convert(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
