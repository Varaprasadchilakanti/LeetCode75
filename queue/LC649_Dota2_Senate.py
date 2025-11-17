"""
649. Dota2 Senate

In the world of Dota2, there are two parties: the Radiant and the Dire.
The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:
Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.
The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.
Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".


Example 1:

Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
Example 2:

Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

Constraints:

n == senate.length
1 <= n <= 104
senate[i] is either 'R' or 'D'.

Topics
String
Greedy
Queue


Developer Insights
Core Idea: This is a queue simulation problem.

Each senator can:
Ban one opponent (removes their future turns).
Announce victory if only their party remains.
Best strategy assumption: Senators always ban the earliest possible opponent to maximize their party’s survival.
Simulation approach:
Maintain two queues: one for Radiant indices, one for Dire indices.
Process round by round:
Compare the front indices of both queues.
The smaller index senator acts first (earlier in order).
That senator bans the opponent and re-enters the queue with index +n (simulating next round).
Continue until one queue is empty → winner is the other party.


Pseudocode

function predictPartyVictory(senate):
    n = len(senate)
    queueR = indices of 'R'
    queueD = indices of 'D'

    while queueR and queueD:
        r = pop from queueR
        d = pop from queueD
        if r < d:
            # Radiant bans Dire, Radiant survives to next round
            push r + n into queueR
        else:
            # Dire bans Radiant, Dire survives to next round
            push d + n into queueD

    return "Radiant" if queueR else "Dire"

"""

from collections import deque
from typing import Protocol

class SenateStrategy(Protocol):
    """Defines contract for senate simulation strategies."""
    def predict(self, senate: str) -> str: ...


class QueueSenateStrategy:
    """
    Queue-based simulation strategy for Dota2 Senate.

    Uses two queues to track Radiant and Dire senators by index.
    In each round, the senator with the smaller index acts first,
    bans the opponent, and re-enters the queue with index + n.
    Continues until one party is eliminated.
    """
    def predict(self, senate: str) -> str:
        n = len(senate)
        queueR, queueD = deque(), deque()

        # Initialize queues with indices
        for i, s in enumerate(senate):
            if s == 'R':
                queueR.append(i)
            else:
                queueD.append(i)

        # Simulate rounds
        while queueR and queueD:
            r, d = queueR.popleft(), queueD.popleft()
            if r < d:
                queueR.append(r + n)  # Radiant survives
            else:
                queueD.append(d + n)  # Dire survives

        return "Radiant" if queueR else "Dire"


class Solution:
    """
    High-level orchestrator for senate simulation.

    Depends on abstraction (SenateStrategy) rather than concrete implementation.
    Default strategy is QueueSenateStrategy, but can inject alternatives.
    """
    def __init__(self, strategy: SenateStrategy = QueueSenateStrategy()) -> None:
        self.strategy = strategy

    def predictPartyVictory(self, senate: str) -> str:
        """
        Predicts the winning party in the Dota2 senate voting process.

        Args:
            senate (str): String of senators ('R' for Radiant, 'D' for Dire).

        Returns:
            str: "Radiant" or "Dire" depending on the winner.
        """
        return self.strategy.predict(senate)


# Usage

solver = Solution()
print(solver.predictPartyVictory("RD"))    # Radiant
print(solver.predictPartyVictory("RDD"))   # Dire
print(solver.predictPartyVictory("RRR"))   # Radiant
print(solver.predictPartyVictory("DDD"))   # Dire
