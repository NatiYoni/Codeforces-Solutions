import sys
import collections
input = sys.stdin.readline

def inp():
    return int(input())



def solve():
    n = inp()
    if n % 3 == 1:
        print("YES")
    else:
        print("NO")
    

def main():
    multi = True
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()