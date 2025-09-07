class Dots:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Dots(x={self.x}, y={self.y})"

def euclidean(d1: Dots, d2: Dots) -> int:
    return int(pow((d2.x - d1.x ) ** 2 + (d2.y - d1.y) ** 2, 0.5))

def sp(dots: list, n: int):
    p1 = p2 = -1
    dmin = float('inf')
    for i in range(n-1):
        for j in range(i+1, n):
            temp = euclidean(dots[i], dots[j])
            if temp < dmin:
                dmin = temp
                p1 = dots[i]
                p2 = dots[j]
    return p1, p2