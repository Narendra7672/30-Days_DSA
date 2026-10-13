# Car Fleet:
def CarFleet(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)

    fleets = 0
    last_time = 0

    for pos, spd in cars:
        time = (target - pos) / spd

        if time > last_time:
            fleets += 1
            last_time = time

    return fleets
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

print(CarFleet(target, position, speed))