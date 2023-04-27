from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: n = 0': [
        0,
        0
    ],
    '2: n = 1': [
        1,
        1
    ],
    '3: n = 2': [
        2,
        1
    ],
    '4: n = 3': [
        3,
        1
    ],
    '5: n = 4': [
        4,
        2
    ],
    '9: n = 9': [
        9,
        3
    ],
    '10: n = 10': [
        10,
        3
    ],
    '11: n = 99': [
        99,
        9
    ],
    '12: n = 100': [
        100,
        10
    ],
    '13: n = 101': [
        101,
        10
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.bulbSwitch(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
