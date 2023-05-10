#Failed Variant 2
#Failed due to time

import itertools

n, k = map(int, input().split())
r_q, c_q = map(int, input().split())
obstacles = []
for i in range(k):
  obstacles.append(tuple(map(int, input().split())))

#Creating a generator which calculates the step that can be taken by the queen
#List/tuple comprehension that receives the steps generated and checks whether such step has any obstacles, if yes break.
ru = ((i, c_q) for i in range(r_q + 1, n + 1)) #north
ru = len(tuple(itertools.takewhile(lambda x: x not in obstacles, ru)))

rd = (((i * -1), c_q) for i in range((r_q * -1) + 1, 0)) #south
rd = len(tuple(itertools.takewhile(lambda x: x not in obstacles, rd)))


cl = ((r_q, i) for i in range(c_q + 1, n + 1)) #west
cl = len(tuple(itertools.takewhile(lambda x: x not in obstacles, cl)))

cr = ((r_q, (i * -1)) for i in range((c_q * -1) + 1, 0)) #east
cr = len(tuple(itertools.takewhile(lambda x: x not in obstacles, cr)))


dlu = ((i, j * -1) for i, j in zip(range(r_q + 1, n + 1), range((c_q * -1) + 1, 0))) #north_west
dlu = len(tuple(itertools.takewhile(lambda x: x not in obstacles, dlu)))

dld = ((i * -1, j * -1) for i, j in zip(range((r_q * -1) + 1, 0), range((c_q * -1) + 1, 0))) #south_west
dld = len(tuple(itertools.takewhile(lambda x: x not in obstacles, dld)))

dru = ((i, j) for i, j in zip(range(r_q + 1, n + 1), range(c_q + 1, n + 1))) #north_east
dru = len(tuple(itertools.takewhile(lambda x: x not in obstacles, dru)))

drd = ((i * -1, j) for i, j in zip(range((r_q * -1) + 1, 0), range(c_q + 1, n + 1))) #north_west
drd = len(tuple(itertools.takewhile(lambda x: x not in obstacles, drd)))

#Finding the steps that can be taken by queen
print (ru + rd + cl + cr + dlu + dld + dru + drd)
