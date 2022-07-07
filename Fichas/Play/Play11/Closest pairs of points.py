import math

def closest_pair(points):
    points = sorted(points, key = lambda x: x[0])
    return calculate(points)
    
 
def calculate(points):
    if len(points) == 2:
        return math.dist(points[0], points[1])
    elif len(points) == 3:
        return min([math.dist(points[0], points[1]), math.dist(points[0], points [2]), math.dist(points[1], points[2])])
    left = points[:len(points)//2]
    right = points[len(points)//2:]
    dLR = min(calculate(left), calculate(right))
    dM = [math.dist(i, j) for i in left for j in right if abs(i[0]-j[0]) < dLR]
    return round(dLR) if dM == [] else round(min(dLR, min(dM)))


print(closest_pair([(2498, 7397), (2168, 8117), (2168, 6677), (1496, 1976), (8893, 9240), (288, 9467), (7465, 8080), (4588, 1774), (4178, 8118), (3459, 7224)]))