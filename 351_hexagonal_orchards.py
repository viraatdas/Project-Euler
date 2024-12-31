from collections import defaultdict



order = 3

points = []

line_params = defaultdict(list)

def build_grid():
    origin_x, origin_y = order, order 
    points.append((origin_x, origin_y))
    print(points)


build_grid()
    
