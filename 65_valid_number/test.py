from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: valid int': [
        '1',
        True
    ],
    '2: valid int with sign': [
        '+1',
        True
    ],
    '3: valid decimal 1': [
        '1.2',
        True
    ],
    '4: valid decimal 2': [
        '1.',
        True
    ],
    '5: valid decimal 3': [
        '.1',
        True
    ],
    '6: valid decimal with sign': [
        '-.1',
        True
    ],
    '7: valid number after exponent': [
        '1e10',
        True
    ],
    '8: valid number with sign after exponent': [
        '1E-2',
        True
    ],
    '9: invalid number with several e': [
        '1e5E',
        False
    ],
    '10: invalid e placement 1': [
        'e34',
        False
    ],
    '10: invalid e placement 2': [
        '34e',
        False
    ],
    '11: invalid sign placement 1': [
        '+',
        False
    ],
    '12: invalid sign placement 2': [
        '+e1',
        False
    ],
    '13: invalid sign placement 3': [
        '6e-',
        False
    ],
    '14: invalid sign placement 4': [
        '-6e8+',
        False
    ],
    '15: invalid sign placement 5': [
        '8+10',
        False
    ],
    '16: invalid sign placement 5': [
        '-+6e20',
        False
    ],
    '17: invalid dot placement 1': [
        '.',
        False
    ],
    '18: invalid dot placement 2': [
        '+.',
        False
    ],
    '19: invalid dot placement 3': [
        '.e10',
        False
    ],
    '20: invalid dot placement 4': [
        '1e+34.67',
        False
    ],
    '21: forbiden symbols': [
        '3a7',
        False
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.isNumber(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
