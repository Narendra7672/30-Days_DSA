# Largest Rectangle in Histogram:
def langest_rect(heights):
    n = len(heights)
    stack = []
    area = 0
    for i,height in enumerate(heights):
        start = i
        while stack and height < stack[-1][0]:
            h ,j = stack.pop()
            w = i - j
            a = h * w
            area = max(area , a)
            start = j
        stack.append((start,height)) 
    while stack:
        h , j= stack.pop()
        w = n - j
        area = max(area,h*w)
    return area
heights = [2, 1, 5, 6, 2, 3]
res = langest_rect(heights)
print(res)       