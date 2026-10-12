# Asteroid Collision:

def AsteroidCollision(asteroid):
    stack = []
    for a in asteroid:
        while stack and a < 0 < stack[-1]:
            if stack[-1] < -a:
                stack.pop()
                continue
            elif stack[-1] == -a:
                stack.pop()
            break
        else:
            stack.append(a)
    return stack
asteroid = [5,10,-5]
res = AsteroidCollision(asteroid)
print(res)            