import matplotlib.pyplot as plt

class point:
    def __init__(self, name, x, y):
        self.name = name
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"{self.name}({self.__x}, {self.__y})"
    
    def get_coordinates(self):
        return self.__x, self.__y

class line:
    def __init__(self, name, p1:point, p2:point):
        self.name = name
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"{self.name}({self.p1}, {self.p2})"
    
    def get_coordinates(self):
        return self.p1.get_coordinates(), self.p2.get_coordinates()


class square:
    def __init__(self, name, l1, l2, l3, l4):
        self.name = name
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4

    def __str__(self):

        return f"{self.name}(\n  {self.l1}, \n  {self.l2}, \n  {self.l3}, \n  {self.l4}\n)"


p1 = point('p1',1, 1)
p2 = point('p2',-1, -1)
p3 = point('p3',1, -1)
p4 = point('p4',-1, 1)

l1 = line('l1', p1, p3)

print(l1.get_coordinates())
l2 = line('l2', p2, p3)
l3 = line('l3', p1, p4)
l4 = line('l4', p4, p2)

s1 = square('s1', l1, l2, l3, l4)

print(p1)
print(p1.get_coordinates())
print(p2)
print(l1)
print(s1)

plt.figure(figsize=(6,6))


# Plot points
points = [p1, p2, p3, p4]
for p in points:
    x, y = p.get_coordinates()
    plt.plot(x, y, 'bo')  # blue dot for points
    plt.text(x, y, f' {p.name}', fontsize=20)  # label the points

# Plot lines
lines = [l1, l2, l3, l4]
for l in lines:
    (x1, y1) , (x2, y2) = l.get_coordinates()
    plt.plot([x1, x2], [y1, y2], 'r-')  # red line for edges
    plt.text((x1+x2)/2, (y1+y2)/2, f' {l.name}', fontsize=20)

# Setting the grid, limits, and aspect ratio
plt.grid(True)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal', adjustable='box')

plt.title("Square with Points and Lines")
plt.show()