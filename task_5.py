#!/usr/bin/env python3

def isPalindromic(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            return False
    return True

S = 0
for n in range(1, 10**6+1):
    binary = str(bin(n))[2:]
    if isPalindromic(n) and isPalindromic(binary):
        print(n, binary)
        S += n

print(S)

