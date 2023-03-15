from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid_addresses = []

        def place_dot(address: str, pointer: int, dots_left: int) -> None:
            if pointer >= len(s):
                return
            if dots_left == 0:
                if s[pointer] == '0' and pointer < len(s) - 1:
                    return
                if int(s[pointer:]) < 256:
                    valid_addresses.append(address + s[pointer:])
                return

            if s[pointer] == '0':
                place_dot(address + '0.', pointer + 1, dots_left - 1)
                return

            next_pointer = pointer + 1
            while (
                    next_pointer <= len(s)
                    and int(s[pointer:next_pointer]) < 256
            ):
                place_dot(
                    address + s[pointer:next_pointer] + '.',
                    next_pointer,
                    dots_left - 1
                )
                next_pointer += 1

        place_dot('', 0, 3)
        return valid_addresses
