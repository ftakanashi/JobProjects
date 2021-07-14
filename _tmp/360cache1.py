import sys

def process(s):
    i = len(s) - 1
    while s[i] == 'a':
        i -= 1
    b_cnt = 0
    ans = 0
    while i >= 0:
        if s[i] == 'b':
            b_cnt += 1
        else:
            ans += b_cnt
            b_cnt *= 2
        i -= 1

    return ans % (10**9 + 7)

def main():
    s = sys.stdin.read().strip()
    res = process(s)
    print(res)

main()