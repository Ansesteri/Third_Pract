N = int(input())
a = [int(s) for s in input().split()]
P = int(input())
print(" ".join([str(x) for x in a if x != P]))