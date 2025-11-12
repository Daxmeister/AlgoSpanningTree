import sys
import math
import random


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
    # Calculates euclidean distance. Hypot is used for speed.
    
    distance = math.hypot(xc[i1]-xc[i2], yc[i1]-yc[i2])
    rounded_dist = int(distance+0.5) # rounds to nearest int
    return rounded_dist

def printer(array):
    # Function used to print to std err
    
    out = sys.stdout.write
    out("\n".join(map(str, array)) + "\n")
        
def greedy_algorithm(x_coords_in, y_coords_in, starting_node=0):
    # This code follows the algorithm from the given task to give us a starting point. It returns a tour and it's length
   
    # Make variables local to speed up (it only went from 0.29-0.28, no big difference, remove?) TODO
    x_coords = x_coords_in
    y_coords = y_coords_in
    
    # Setup
    n = len(x_coords)
    tour = [starting_node]
    used = [False]*n
    used[starting_node] = True
    tour_length = 0
    
    # Run the greedy/naive algorithm
    for i in range(1, n):
        best = -1
        for j in range(0, n):
            if used[j] == False and (best == -1 or dist(x_coords, y_coords, tour[i-1], j) < best_w):
                 best = j
                 best_w = dist(x_coords, y_coords, tour[i-1], best) # To avoid recomputing it with every run of j
        
        tour.append(best)
        used[best] = True
        tour_length += best_w
        
    return tour, tour_length


def multiple_random_starts(x_coords, y_coords, number_of_starts=1):
    # This function runs the greedy algorithm with different, random, starts. Returns shortest path.
    # However, there was not time to run it more than once in kattis!!!
    
    
    best_path = [[], sys.maxsize]
    n = len(x_coords)
    
    # Generate random starts
    random_numbers = random.sample(range(1, n), number_of_starts-1) #n+1 ensures that we can start on last node, we remove one form number_of_starts because we always add 0
    random_numbers.append(0) # 0 is the reference, we never want to be worse
    
    # Run the algorithm starting form different nodes
    for i in range(len(random_numbers)): # We start once for every random number
        tour, cost_of_path = greedy_algorithm(x_coords, y_coords, random_numbers[i])
        if cost_of_path < best_path[1]:
            best_path[0] = tour
            best_path[1] = cost_of_path
    
    # print(best_path[1])        
    return best_path[0]

def main():
    # Read input coordinates
    x_coords, y_coords = read_input()
    
    # Get the fastest tour
    tour = multiple_random_starts(x_coords, y_coords, 1)
    
    # Print to stdout
    printer(tour)


main()