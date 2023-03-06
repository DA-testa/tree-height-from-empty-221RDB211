# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    height = [0]*n
    for node in range(n):
        if parents[node] == -1:
            height[node] = 1
        else:
            parent_height = height[parents[node]]
            height[node] = parent_height + 1
    return max(height)
    


def main():
    n = int(input())
    parents = np.array(list(map(int, input().split())))

    height = compute_height(n, parents)
    print(height)
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
