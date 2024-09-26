def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

print(gcd(22, 9999))
