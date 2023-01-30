from solution import solution


TEST_VALUES = {
    '1 common prefix exists': [
        ['flower', 'flow', 'flight'],
        'fl'
    ],
    '2: no common prefix': [
        ['dog', 'racecar', 'car'],
        ''
    ],
    '3: empty string': [
        [''],
        ''
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.longestCommonPrefix(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
