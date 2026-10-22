# Maximum Profit in Job Scheduling with Multiple Machines:
import heapq


def jobSchedulingMultipleMachines(startTime,endTime,profit,M):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x)
    machines = [(0, 0) for _ in range(M)]
    max_profit_so_far = 0
    for s, e, p in jobs:
        best_prev_profit = -1
        best_machine_idx = -1
        for i in range(len(machines)):
            end_time, cum_profit = machines[i]
            if end_time <= s:
                if cum_profit > best_prev_profit:
                    best_prev_profit = cum_profit
                    best_machine_idx = i
        if best_machine_idx != -1:
            end_time, cum_profit = machines[best_machine_idx]
            new_profit = cum_profit + p
            machines[best_machine_idx] = (e, new_profit)
            max_profit_so_far = max(max_profit_so_far, new_profit)
            heapq.heapify(machines)
    return max(cum_profit for _, cum_profit in machines)


startTime = [1, 2, 3, 5]
endTime = [3, 5, 6, 7]
profit = [50, 20, 70, 30]
M = 2
print(jobSchedulingMultipleMachines(startTime, endTime, profit, M))
