from asyncio.windows_events import NULL
import sys
import fileinput

List1 = []
List2 = []
Result = []

datafile = open("data.txt")

for line in datafile:
    first, second = map(int, line.strip().split())
    List1.append(first)
    List2.append(second)

List1.sort()
List2.sort()
iter = 0
SimScore = 0

for i in range(len(List1)):
    for j in range(len(List2)):
        if(List2[j]==List1[i]):
            iter = iter + 1
    SimScore = SimScore + List1[i] * iter
    iter = 0

for i in range(len(List1)):
    Result.append(abs(List1[i]-List2[i]))
    
print(List1[:5])
print(List2[:5])
print(Result[:5])
print(sum(Result))
print(SimScore)
    
    
    
