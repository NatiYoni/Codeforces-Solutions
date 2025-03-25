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
    # solution here

    n, m = invr()
    s = []
    for i in range(n):
        s.append(insr())

    row_xor = [0] * n
    col_xor = [0] * m

    for i in range(n):
            for j in range(m):
                value = int(s[i][j])
                row_xor[i] ^= value
                col_xor[j] ^= value
    
    row = sum(1 for x in row_xor if x == 1)
    col = sum(1 for x in col_xor if x == 1)

    print(max(row,col))
    
    
    
    
    
        
    
    # print(arr)
    pass

def main():
    multi = True # if multiple Test cases change it to true
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()