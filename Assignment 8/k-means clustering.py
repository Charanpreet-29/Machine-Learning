import sys
import random
import math


datafile = sys.argv[1]
f = open(datafile)
data = []
i = 0
l = f.readline()

while (l != ''):
    l = l.strip('\n')
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()
rows = len(data)
cols = len(data[0])
f.close()


mean = int(input('Number of clusters'))
col = [0 for _ in range(0, cols, 1)]
euc_dist = [col for _ in range(0, mean, 1)]
value = 0

for i in range(0, mean, 1):
    value = random.randrange(1, rows-1)
    euc_dist[i] = data[value]
trainlabels = {}
difference = 1

prev = [[0]*cols for i in range(mean)]
mdist = [0 for _ in range(0, mean, 1)]

n = [0.1 for _ in range(0, mean, 1)]
distance = [0.1 for _ in range(0, mean, 1)]


tot_dist = 1
classes = []

while ((tot_dist) > 0):
    for i in range(0, rows, 1):
        distance = []

        for k in range(0, mean, 1):
            distance.append(0)

        for k in range(0, mean, 1):
            for j in range(0, cols, 1):
                distance[k] += ((data[i][j] - euc_dist[k][j])**2)

        for k in range(0, mean, 1):
            distance[k] = (distance[k])**0.5

        mindist = 0
        mindist = min(distance)
        for k in range(0, mean, 1):
            if(distance[k] == mindist):
                trainlabels[i] = k
                n[k] += 1
                break

    euc_dist = [[0]*cols for g in range(mean)]
    col = []

    for i in range(0, rows, 1):
        for f in range(0, mean, 1):
            if(trainlabels.get(i) == f):
                for j in range(0, cols, 1):
                    dist = euc_dist[f][j]
                    point = data[i][j]
                    euc_dist[f][j] = dist + point
    for j in range(0, cols, 1):
        for i in range(0, mean, 1):
            euc_dist[i][j] = euc_dist[i][j]/n[i]

    classes = [int(i) for i in n]
    n = [0.1]*mean

    mdist = []
    for f in range(0, mean, 1):
        mdist.append(0)
    for f in range(0, mean, 1):
        for c in range(0, cols, 1):
            mdist[f] += float((prev[f][c]-euc_dist[f][c])**2)

        mdist[f] = (mdist[f])**0.5

    prev = euc_dist
    tot_dist = 0
    for i in range(0, len(mdist), 1):
        tot_dist += mdist[i]

    print("Combined distances between means are", tot_dist)
print("For k = ", mean, "the final means are", classes)

for h in range(0, rows, 1):
    print(trainlabels[h], h)