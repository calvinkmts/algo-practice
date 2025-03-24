from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        remaining_fuel = [gas[i] - cost[i] for i in range(len(gas))]

        starting_index = -1
        starting_fuel = 0

        for i in range(len(remaining_fuel)):
            if starting_index == -1:
                starting_index = i

            starting_fuel += remaining_fuel[i]

            if starting_fuel < 0:
                starting_index = -1
                starting_fuel = 0

        return starting_index