from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        hp = [-c for c in count.values()]
        timer = 0
        heapq.heapify(hp)
        while hp or q:
            timer += 1
            # pop a maximum count of object from the heap
            if hp:
                c = heapq.heappop(hp)
                # if it is not equal to zero we push it to priority queue
                if c + 1 != 0:
                    # object in q : (count - 1, current time + cooldown time)
                    q.append((c + 1, timer + n))
                    # means EXECUTED a task

            # if the first item in the queue is finished cooldown
            if q and q[0][1] == timer:
                curr, _ = q.popleft()
                # add the item in the heap
                heapq.heappush(hp, curr)
            
        return timer








if __name__ == "__main__":
    s = Solution()
    print(s.leastInterval(tasks=["A","A","A", "B","B","B"], n = 3))