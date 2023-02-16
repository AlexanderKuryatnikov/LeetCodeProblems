from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: intersecting arrays': [
        [1, 2, 3, 0, 0, 0],
        3,
        [2, 5, 6],
        3,
        [1, 2, 2, 3, 5, 6]
    ],
    '2: nums2 is empty': [
        [1],
        1,
        [],
        0,
        [1]
    ],
    '3: nums1 is empty': [
        [0],
        0,
        [1],
        1,
        [1]
    ],
    '4: nums1 before nums2': [
        [0, 1, 2, 3, 0, 0, 0],
        4,
        [5, 6, 6],
        3,
        [0, 1, 2, 3, 5, 6, 6]
    ],
    '5: nums2 before nums1': [
        [0, 1, 2, 0, 0, 0, 0],
        3,
        [-3, -2, -1, 0],
        4,
        [-3, -2, -1, 0, 0, 1, 2]
    ],
    '6: num1 inside nums2': [
        [2, 4, 6, 0, 0, 0, 0],
        3,
        [1, 3, 4, 5],
        4,
        [1, 2, 3, 4, 4, 5, 6]
    ],
    '7: nums2 inside nums1': [
        [1, 3, 5, 6, 8, 0, 0, 0],
        5,
        [2, 4, 7],
        3,
        [1, 2, 3, 4, 5, 6, 7, 8]
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        solution.merge(values[0], values[1], values[2], values[3])
        assert values[0] == values[4], f'Test {test}. Your result {values[0]}'
        print(f'Test {test}... OK')
