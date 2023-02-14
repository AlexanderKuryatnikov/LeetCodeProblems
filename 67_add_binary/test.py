from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: first longer': [
        '10100',
        '101',
        '11001'
    ],
    '2: second longer': [
        '101',
        '10100',
        '11001'
    ],
    '3: new digit place 1': [
        '11',
        '1',
        '100'
    ],
    '4: new digit place 2': [
        '1010',
        '1011',
        '10101'
    ],
    '5: domino': [
        '1',
        '11111',
        '100000'
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.addBinary(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
