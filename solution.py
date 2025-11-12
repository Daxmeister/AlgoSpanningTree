import sys
import math


def read_input():
    # Function reads from std input from kattis and returns coordinates as two arrays of floats
    n = int(sys.stdin.readline())
    xc = []
    yc = []
    for i in range(n): 
        x, y = sys.stdin.readline().split()
        xc.append(float(x))
        yc.append(float(y))
    return xc, yc

def dist(xc, yc, i1, i2):
    distance = math.hypot(xc[i1]-xc[i2], yc[i1]-yc[i2])
    rounded_dist = int(distance+0.5) # rounds to nearest int
    return rounded_dist

def printer(array):
    for element in array:
        print(element)
        
def greedy_algorithm(x_coords, y_coords, starting_node=0):
    tour = [0]
    used = set()
    used.add(0)
    n = len(x_coords)
    # Run the greedy/naive algorithm
    for i in range(1, n):
        best = -1
        for j in range(0, n):
            if j not in used and (best == -1 or dist(x_coords, y_coords, tour[i-1], j) < dist(x_coords, y_coords, tour[i-1], best)):
                 best = j
        
        tour.append(best)
        used.add(best)
    return tour

def main():
    # Read input coordinates
    x_coords, y_coords = read_input()
    tour = greedy_algorithm(x_coords, y_coords)
    printer(tour)
                 
                



main()