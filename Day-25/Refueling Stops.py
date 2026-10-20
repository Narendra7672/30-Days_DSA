import heapq

def minRefuelStops(target: int, startFuel: int, stations: list[list[int]]) -> int:
    max_heap = []
    ans = 0
    prev_pos = 0
    current_fuel = startFuel
    stations = stations + [[target, 0]]
    for pos, fuel in stations:
        distance = pos - prev_pos
        current_fuel -= distance
        while current_fuel < 0 and max_heap:
            current_fuel += -heapq.heappop(max_heap)
            ans += 1
        if current_fuel < 0:
            return -1
        heapq.heappush(max_heap, -fuel)
        prev_pos = pos
    return ans
target = 100
startFuel = 10
stations = [[10, 60],[20, 30],[30, 30],[60, 40]]
print(minRefuelStops(target, startFuel, stations))