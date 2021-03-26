def isPrime(n):
    if n <= 1: return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def countPrimeStrings(inputString):
    #WRITE YOUR CODE HERE

    s = inputString
    mem = {}

    def dfs(res, start):
        if start == len(s): return 1
        if s[start] == '0': return 0
        if start in mem: return mem[start]
        count = 0
        for end in range(start, len(s)):
            if end > start and s[end] in '02468': continue
            num = int(s[start:end+1])
            if num > 10**6: break
            if isPrime(num):
                res.append(num)
                count += dfs(res, end + 1)
                res.pop()

        mem[start] = count
        return count

    return dfs([], 0) % (10**9 + 7)

if __name__ == '__main__':
    res = countPrimeStrings('1137311373113731137311373113731137311373113731137311373')
    print(res)