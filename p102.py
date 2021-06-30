# Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

# Consider the following two triangles: A(-340,495), B(-153,-910), C(835,-947) X(-175,41), Y(-421,-714), Z(574,-645)

# It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

# Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

# https://projecteuler.net/project/resources/p102_triangles.txt

with open("data/p102_triangles.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        verts = list(map(int, line.strip().split(",")))
        x1, y1, x2, y2, x3, y3 = verts
        if y1 * x2 > y2 * x1:
            if y1 * x3 < y3 * x1 and y2 * x3 > y3 * x2:
                sum += 1
        else:
            if y1 * x3 > y3 * x1 and y2 * x3 < y3 * x2:
                sum += 1

    print(sum)