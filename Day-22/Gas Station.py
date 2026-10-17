#Gas Station:

def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    total_tank, current_tank, start_index = 0, 0, 0

    for i in range(len(gas)):
        net_gas = gas[i] - cost[i]
        total_tank += net_gas
        current_tank += net_gas

        if current_tank < 0:
            start_index = i + 1
            current_tank = 0

    return start_index if total_tank >= 0 else -1
print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))