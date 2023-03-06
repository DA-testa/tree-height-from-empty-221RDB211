# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    parents = np.array(parents)
    heights = np.zeros(n, dtype=int)
    def compute_subtree_height(node):
        if not np.any(parents == node):
            heights[node] = 1
            return 1
        height = 1 + np.max(compute_subtree_height(child) for child in np.where(parents == node)[0])
        heights[node] = height
        return height
    root = np.where(parents == -1)[0][0]
    compute_subtree_height(root)
    return np.max(heights)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)   
threading.Thread(target=main).start()
main()
