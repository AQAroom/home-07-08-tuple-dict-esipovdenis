r = int(input())
g = int(input())
b = int(input())
color = (r, g, b)
# grey = (color[0], color[1], color[2])
if color[0] == color[1] == color[2]:
    print("Да")
else:
    print("Нет")
