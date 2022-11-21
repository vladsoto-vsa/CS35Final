
# From most efficient to least efficient
#
# constant time: O(1)      always the same time, no matter what N
#   logarithmic: O(lgN)    time increases as lg(N)
#        linear: O(N)      if you double N, you would double the time
#     loglinear: O(NlgN)   combination of logarithmic and linear
#     quadratic: O(N^2)    if you double N, you would quadruple the time

# How many "steps" for each of the following?
# What happens to the number of steps when N --> 2N?

#############################################
# 1
print("1"*50)
N = int(input("N: "))
for i in range(N):
    print(i)
# Answer: O(n)
#############################################
# 2
print("2"*50)
N = int(input("N: "))
for i in range(100):
    print(i*N)
#Answer: Loop always runs 100 times, so 0(1)
#############################################
# 3
print("3"*50)
N = int(input("N: "))
for i in range(N):
    print(i)
for j in range(N):
    print(j)

#Answer: first loop takes N Steps, second loop takes N steps, N+N= 2

#############################################
# 4
print("4"*50)
N = int(input("N: "))
for i in range(N):
    for j in range(N):
        print(i, j)
#Answer: Outer loop runs N times, and each iteration of outer loop
#runs the inner loop, and the inner lopp runs N times. N*N is O(n^2)

#############################################
# 5
print("5"*50)
N = int(input("N: "))
for i in range(N):
    for j in range(i,N):
        print(i, j)
#Answer: The inner loop runs a different amount each time
#N + (N-1) + (N-2)...
# this summation: N(N+1)/2 = N^2/2 + N/2 = 0(N^2)

#############################################
# 6
print("6"*50)
N = int(input("N: "))
for i in range(N):
    for j in range(10):
        print(i, j)
#Answer: N*10 = O(N)

#############################################
# 7
print("7"*50)
N = int(input("N: "))
while N > 1:
    print(N)
    N = N/2
#Answer:Like binary search O(lgN)

#############################################
# 8
print("8"*50)
L = [1,2,5,7,13,21,24,25,26,33,34,38,50,57,58,63]
N = len(L)
mid = N//2
print(L[mid])

#Answer: Constant O(1)

#############################################
# 9
print("9"*50)
N = int(input("N: "))
for i in range(N):
    k = N
    while k > 1:
        print(i, k)
        k = k/2
#Answer: Outer loop runs N times, inner loop runs lg(N)
#The whole thing is O(NlgN)
#############################################
