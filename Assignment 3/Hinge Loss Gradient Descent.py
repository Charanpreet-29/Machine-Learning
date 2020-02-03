import sys
import random

def normalize(datafile):
    max = []
    min = []

    for i in range(len(datafile[0])):
        max.append(0)
        min.append(0)
        
    for j in range(len(datafile)):
        for k in range(len(datafile[0])-1):
            if (datafile[j][k] > max[k]) :
                max[k] = datafile[j][k]
            if (datafile[j][k] < min[k]) :
                min[k] = datafile[j][k]

    for i in range(len(datafile)):
        for j in range(len(datafile[0])-1):
            if (max[j] - min[j] != 0):
                datafile[i][j] = (datafile[i][j] - min[j])/(max[j] - min[j])
    return datafile
    
datafile = sys.argv[1]
f = open (datafile)#""ionosphere""


data = []
i = 0
l = f.readline()

while(l != '') :
    a = l.split()
    b = len(a)
    l2 = []
    for j in range(0, b, 1):
        l2.append(float(a[j]))
        if j == (b-1) :
            l2.append(float(1))

    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])

maxd = 0
mind = 0
normal = 0
for i in range(cols):
    maxd = max(data[0])
    if (maxd > 1):
        normal = 1

if normal == 1 :
    data = normalize(data)

f.close()
#--------------------------------------------------------------
##read label data
labelfile = sys.argv[2]
f = open(labelfile)#"ionosphere.trainlabels.0"
# f = open("ionosphere.trainlabels.0")

trainlabels = {}
n = []
n.append(0)
n.append(0)

l = f.readline()
while(l != '') : #read

    a = l.split()
    if int(a[0]) == 0:
        trainlabels[int(a[1])] = -1
    else:
        trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1

w = []
for j in range(cols):
    w.append(0)
    w[j] = (0.02 * random.uniform(0,1)) - 0.01

def dot_prod(list1, list2):
    dp = 0
    for j in range(len(list1)):
        dp += list1[j] * list2[j]
    return dp


delf = []
for i in range(cols):
    delf.append(0)


eta = 0.001


flag = 0
k=0
y_d_p = 0


error=0.0
for i in range (rows):
    if(trainlabels.get(i) != None):
        y_d_p = (trainlabels.get(i))*dot_prod(w,data[i])
        error += max(0.0, (1.0 - y_d_p))
        

while(flag != 1):
    k+=1
    delf = []
    for i in range(cols):
        delf.append(0)

    for i in range(rows):
        if(trainlabels.get(i) != None):
            d_p = dot_prod(w, data[i])
            y_d_p = (trainlabels.get(i)*dot_prod(w,data[i]))
            
            for j in range (cols):
                 if ( y_d_p < 1):
                     delf[j] += (-1 * (trainlabels.get(i) * data[i][j]))
                 elif(y_d_p >= 1):
                     delf[j] += 0
    for j in range(cols):
        w[j] = w[j] - eta*delf[j]
    curr_error = 0
    for i in range (rows):
        if(trainlabels.get(i) != None):
            y_d_p = (trainlabels.get(i))*dot_prod(w,data[i])
            curr_error += max(0, (1.0 - y_d_p))
            if(abs(error - curr_error)<eta):
                eta = 0.1*eta

    if abs(error - curr_error) < 0.001:
        flag = 1
    error = curr_error


for i in range(rows):
    if(trainlabels.get(i) == None):
        d_p = dot_prod(w, data[i])
        if(d_p > 0):
            print("1",i)
        else:
            print("0",i)
