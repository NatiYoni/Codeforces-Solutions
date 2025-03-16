t = int(input())
outputs = []

for _ in range(t):
    n = int(input())
    s = input()
    temp = "0"
    ans = 0

    for i in range(n):
        if s[i] != temp:
            ans += 1
            temp = s[i]
    outputs.append(ans)

for output in outputs:
    print(output)
            
