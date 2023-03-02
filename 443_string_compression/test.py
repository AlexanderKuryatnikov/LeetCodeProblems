from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: repeating chars': [
        ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
        6
    ],
    '2: single char': [
        ['a'],
        1
    ],
    '3: multiple digits repeating char': [
        ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
        4
    ],
    '4: last char is single': [
        ['a', 'a', 'a', 'b'],
        3
    ],
    '5: repeating numbers': [
        ['1', '1', '1', '2', '3', '3'],
        5
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.compress(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
