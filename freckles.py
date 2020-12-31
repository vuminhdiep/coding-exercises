import sys
import heapq
from math import sqrt


def load_int():
    return int(sys.stdin.readline())


def load_floats():
    line = sys.stdin.readline()
    return list(map(float, line.split()))


def load_case():
    sys.stdin.readline()
    nfreckles = load_int()

    freckles = []
    for n in range(nfreckles):
        freckles.append(tuple(load_floats()))

    return freckles


def point_dist(v1, v2):
    return sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)


def min_tree(points):
    vertices = [0, ]
    edges = []
    free = [(99999999999, i + 1, 0) for i, v in enumerate(points[1:])]

    def update_free(vertex):

        coordv = points[vertex]
        for i, f in enumerate(free):
            dist, fvertex, _ = f
            coordf = points[fvertex]
            ndist = point_dist(coordf, coordv)
            if ndist < dist:
                free[i] = (ndist, fvertex, vertex)

        heapq.heapify(free)

    update_free(0)

    while free:
        dist, fvertex, vertex = heapq.heappop(free)
        vertices.append(fvertex)
        edges.append((vertex, fvertex))

        update_free(fvertex)

    return vertices, edges


if __name__ == '__main__':

    ncases = load_int()

    for c in range(ncases):
        points = load_case()
        vertices, edges = min_tree(points)

        length = sum([point_dist(points[s], points[e]) for s, e in edges])
        print("{0:.2f}".format(length))

        if c + 1 < ncases:
            print('')