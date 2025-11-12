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

def main():
    x_coords, y_coords = read_input()
    for i in range(len(x_coords)):
        dist(x_coords, y_coords, i, 2)   


main()