x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point = (x1, y1)
point_2 = (x2, y2)
distance = ((point_2[0] - point[0]) ** 2 + (point_2[1] - point[1]) ** 2) ** 0.5
print(f"{distance:.2f}")
