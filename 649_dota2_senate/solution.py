from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        r_banned = 0
        d_banned = 0
        while True:
            if r_banned >= len(queue):
                return 'Dire'
            if d_banned >= len(queue):
                return 'Radiant'

            senator = queue.popleft()
            if senator == 'R':
                if r_banned:
                    r_banned -= 1
                else:
                    d_banned += 1
                    queue.append(senator)
            else:
                if d_banned:
                    d_banned -= 1
                else:
                    r_banned += 1
                    queue.append(senator)
