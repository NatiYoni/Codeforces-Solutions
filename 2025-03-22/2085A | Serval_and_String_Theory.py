import sys, collections, math, random

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input())
invr = lambda: map(int, input().split())

def dd(type_func=int):
    return collections.defaultdict(type_func)

def is_in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

rand_no = random.randint(1, 1000000000)

def solve():

    n , k= invr()
    s = insr()
    set_ = set(s)
    # print(set_)
    if len(set_) == 1:
        print("NO")

    elif ord(s[0]) < ord(s[-1]):
        print("YES")
         
    elif k > 0:
        print("YES")
    
    elif s < s[::-1]:
        print("YES")

    else:
        print("NO")
    
    pass

def main():
    multi = True  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()