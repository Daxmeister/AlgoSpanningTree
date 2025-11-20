import sys
import math
import random # for multiple starts

def read_input():
    N = int(sys.stdin.readline()) 

    x = [0.0] * N
    y = [0.0] * N

    for i in range(N):
        x_str, y_str = sys.stdin.readline().split()
        x[i] = float(x_str)
        y[i] = float(y_str)
        
    return x, y, N


def dist(i, j, x, y):
    return math.sqrt ((x[j]-x[i])**2 + (y[j]-y[i])**2)


def build_dist(x, y, N):
    dist = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = math.sqrt ((x[j]-x[i])**2 + (y[j]-y[i])**2)
    return dist
    
    
def greedy_tour(dist, N, start=0):
    tour = [0] * N
    used = [False] * N
    
    tour_length = 0
    tour[0] = start
    used[start] = True
    
    for i in range(1, N):
        best = -1
        for j in range(N):
            if (not used[j]) and (best == -1 or dist[tour[i-1]][j] < dist[tour[i-1]][best]):
                best = j
        tour[i] = best
        used[best] = True
        tour_length += dist[tour[i-1]][tour[i]]
    return tour, tour_length
            
            
def two_opt(tour, dist):
    # Implements two-opt
    EPS = 1e-9
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                a,b,c,d = tour[i-1], tour[i], tour[j], tour[j+1]
                if dist[a][b] + dist[c][d] > dist[a][c] + dist[b][d] + EPS:
                    # reverse the path between i and j
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

def three_opt(tour, dist, N):
    # Implements three-opt
    
    improved = True
    while improved:
        improved = False
        for i in range(1, N-4):
            if improved: # added because break only jumps out of "one level of loop"
                break
            for j in range(i+1, N-3):
                if improved: # added because break only jumps out of "one level of loop"
                    break
                for k in range(j+1, N-2):
                    
   
                    # edges that we remove
                    a = tour[i-1]
                    b = tour[i]
                    c = tour[j]
                    d = tour[j+1]
                    e = tour[k]
                    f = tour[k+1]
                    
                    # Length of removed edges
                    shortest_length = dist[a][b]+dist[c][d]+dist[e][f] 
                    
                    # Note that we cut before i, after j and after k. All four sets must be non-empty since
                    # c3 loops back to c0. This also means that we never cut the edge from c3 to c0.
                    
                    
                    
               
                    # We define the 7 new possible paths, and the 3 edges that are added for each
                    options = [
                        [0,[a,c],[b,d],[e,f]],
                        [0,[a,b],[c,e],[d,f]],
                        [0,[a,c],[b,e],[d,f]],
                        [0,[a,d],[e,b],[c,f]],
                        [0,[a,e],[d,b],[c,f]],
                        [0,[a,d],[e,c],[b,f]],
                        [0,[a,e],[d,c],[b,f]],   
                    ]
                    best_path = -1
                    for l in range(len(options)):
                        option = options[l]
                        added_edge_length = dist[option[1][0]][option[1][1]] + dist[option[2][0]][option[2][1]] + dist[option[3][0]][option[3][1]]
                        if added_edge_length < shortest_length:
                            best_path=l #set the best path
                            shortest_length=added_edge_length #remember the length
                            
                        
                    if best_path>=0: #If we have updated it
                                            # Splitting a tour by removing 3 edges creates 4 components (actually 3, since it is a cycle)
                        c0 = tour[:i]
                        c1 = tour[i:j+1]
                        c2 = tour[j+1:k+1]
                        c3 = tour[k+1:]
                        paths = [ # We calculate the actual tours only now
                                    c0+c1[::-1]+c2+c3,
                                    c0+c1+c2[::-1]+c3,
                                    c0+c1[::-1]+c2[::-1]+c3,
                                    c0+c2+c1+c3,
                                    c0+c2[::-1]+c1+c3,
                                    c0+c2+c1[::-1]+c3,
                                    c0+c2[::-1]+c1[::-1]+c3,   
                                        ]
                        tour = paths[best_path]
                        improved = True
                        break

                    
              
    return tour
                    


def output(tour):
    for i in tour:
        print(i)
    sys.stdout.flush()

def multiple_starts(dist, N, starts=1):
    starts = min(starts, N)
    best_path = [[], sys.maxsize]
    
    # Generate random starts
    random_numbers = random.sample(range(1, N), starts-1)
    random_numbers.append(0) # 0 is the reference, we never want to be worse
    for i in random_numbers: # We start once for every random number
        tour, cost_of_path = greedy_tour(dist, N, i)
        if cost_of_path < best_path[1]:
            best_path[0] = tour
            best_path[1] = cost_of_path
    
    # print(best_path[1])        
    return best_path[0]

def multiple_starts_returnall(dist, N, starts=1):
    starts = min(starts, N)
    paths = []
    
    # Generate random starts
    random_numbers = random.sample(range(1, N), starts-1)
    random_numbers.append(0) # 0 is the reference, we never want to be worse
    for i in random_numbers: # We start once for every random number
        tour, cost_of_path = greedy_tour(dist, N, i)
        paths.append(tour)
    
    # print(best_path[1])        
    return paths


def length_tour(tour, dist):
    length = 0
    length += dist[tour[0]][tour[len(tour)-1]]
    for i in range(1, len(tour)-1):
        length += dist[tour[i-1]][tour[i]]
    return length    
    
def main_old():
    x, y, N = read_input()
    dist = build_dist(x, y, N)
    tour = multiple_starts(dist, N, 2)
    tour = two_opt(tour, dist)
    if N < 1000:
        tour = three_opt(tour, dist, N) 
    output(tour)

def main():
    x, y, N = read_input()
    dist = build_dist(x, y, N)
    tours = multiple_starts_returnall(dist, N, 5)
    best_path = [[], sys.maxsize]
    for tour in tours:
        tour = two_opt(tour, dist)
        tour_length = length_tour(tour, dist)
        if N < 120:
            tour = three_opt(tour, dist, N) 
            tour_length = length_tour(tour, dist)
            
        if tour_length < best_path[1]:
            best_path[0] = tour
            best_path[1] = tour_length
       
    output(best_path[0])


main()