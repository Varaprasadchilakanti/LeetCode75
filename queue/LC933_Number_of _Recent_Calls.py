"""
933. Number of Recent Calls

You have a RecentCounter class which counts the number of recent requests within a certain time frame.
Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3


Constraints:

1 <= t <= 109
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.

Topics
Design
Queue
Data Stream


Key Developer Insights
Core Responsibility: Maintain a sliding window of requests within the last 3000 ms.
Data Structure Choice: A queue (deque) is ideal since we only append new requests and remove outdated ones from the front.

Constraints:

t is strictly increasing → monotonic property ensures efficient cleanup.
At most 10^4 calls → queue operations are safe and performant.

Pseudocode (with conventions)

class RecentCounter:
    initialize empty queue

    function ping(t):
        push t to queue
        while queue not empty and queue[0] < t - 3000:
            pop from front
        return length(queue)


Invariant: After the loop, all elements satisfy 𝑡𝑖≥𝑡−3000, and trivially 𝑡𝑖≤𝑡 since t is strictly increasing.
Edge handling: No special cases needed due to guarantees in the prompt.


Key Takeaways for Developers
Avoid mutable defaults: Always use None and instantiate inside __init__.
Isolate responsibilities: Strategy handles logic, orchestrator handles orchestration.
Preserve invariants: Explicitly document loop invariants in docstrings.
Design for extension: Strategy pattern allows swapping implementations without touching orchestrator.
Traceability: Docstrings explain intent, invariants, and complexity.

"""

from collections import deque
from typing import Protocol, Optional

class CounterStrategy(Protocol):
    """
    Interface Segregation Principle (ISP):
    Defines the contract for counting recent requests.
    Any concrete strategy must implement `ping(t: int) -> int`.
    """
    def ping(self, t: int) -> int: ...


class QueueCounterStrategy:
    """
    Queue-based sliding window strategy for counting recent requests.

    Responsibilities:
    - Maintain a deque of request timestamps.
    - Enforce invariant: after each ping, all timestamps satisfy t - window <= time <= t.
    - Provide O(1) amortized performance by appending new requests and evicting outdated ones.

    Attributes:
        window (int): Size of the time window in milliseconds (default 3000).
        q (deque[int]): Stores timestamps of recent requests.
    """
    def __init__(self, window: int = 3000) -> None:
        self.window = window
        self.q = deque()

    def ping(self, t: int) -> int:
        """
        Add a new request at time t and return the number of requests
        within the inclusive range [t - window, t].

        Args:
            t (int): Timestamp of the new request.

        Returns:
            int: Count of requests in the last `window` milliseconds.
        """
        self.q.append(t)
        boundary = t - self.window
        while self.q and self.q[0] < boundary:
            self.q.popleft()
        return len(self.q)


class RecentCounter:
    """
    High-level orchestrator for counting recent requests.

    Dependency Inversion Principle (DIP):
    - Depends on abstraction (`CounterStrategy`), not concrete implementation.
    - Default strategy is `QueueCounterStrategy`, but can inject alternatives.

    Attributes:
        strategy (CounterStrategy): The injected strategy handling core logic.
    """
    def __init__(self, strategy: Optional[CounterStrategy] = None) -> None:
        # Avoid mutable default trap: instantiate fresh strategy if none provided.
        self.strategy = strategy if strategy is not None else QueueCounterStrategy()

    def ping(self, t: int) -> int:
        """
        Delegate to the injected strategy to process the request.

        Args:
            t (int): Timestamp of the new request.

        Returns:
            int: Count of requests in the last 3000 milliseconds.
        """
        return self.strategy.ping(t)


# Usage

recentCounter = RecentCounter()
print(recentCounter.ping(1))     # 1
print(recentCounter.ping(100))   # 2
print(recentCounter.ping(3001))  # 3
print(recentCounter.ping(3002))  # 3
