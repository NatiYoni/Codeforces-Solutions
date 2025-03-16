import sys
import collections
input = sys.stdin.readline

def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    return list(input().strip())
def invr():
    return map(int, input().split())

# Defaultdict for handling missing keys automatically
def dd_int():
    return collections.defaultdict(int)
def dd_list():
    return collections.defaultdict(list)
def dd_set():
    return collections.defaultdict(set)

def is_in_bounds(grid, i, j):
   return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve():
    arr = inlt()
    a3 = {arr[2] - arr[1], arr[3] - arr[2], arr[0] + arr[1]}

    
    max_count = 0
    for num in a3:
        count = 0
        if num == arr[0] + arr[1]:
                count += 1
        if arr[2] == arr[1] + num:
            count += 1
        if arr[3] == arr[2] + num:
            count += 1
    
        max_count = max(max_count, count)

    print(max_count)
pass

def main():
    multi = True 
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()