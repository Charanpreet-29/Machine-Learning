import sys
import numpy as np
import random


###Reading Data from file
vote_zero = {}
vote_one = {}
datafile = sys.argv[1]
f = open(datafile)
data = []
line = f.readline()
while(line != ''):
    row = line.split( )
    l2 = []
    for i in range(0,len(row),1):
        l2.append(float(row[i]))
    data.append(l2)
    line = f.readline()
rows = len(data)
cols = len(data[0])
f.close()


###Reading Labels from file
bags = []
label_file = sys.argv[2]
f = open(label_file)
train_labels = {}
line = f.readline()
num = [0,0]
while(line != ''):
    row = line.split( )
    train_labels[int(row[1])] = int(row[0])
    data[int(row[1])].append(int(row[0]))

    bags.append(int(row[1]))
    line = f.readline()
    num[int(row[0])] += 1

#print(bags)
for i in range(0,rows,1):
    vote_zero[i] = 0
    vote_one[i] = 0

for d in range(0,100,1):
    low = 100000

    test = []
    sort_data = []
    bag_new = np.random.choice(bags, size=len(bags), replace=True)
    for i in bag_new:
        sort_data.append(data[int(i)])
    for i in range(0,len(sort_data[0]),1):
        test.append((sort_data[len(sort_data)-1][i]+1))
    sort_data.append(test)

    categ_list = []
    col_gin = []
    col_thresh = []
    ginvals = []
    threshbig = []
    for j in range(0,cols,1):
        gini = 1000000000
        thresh = []
        gini_val = []
        def key_func(e):
            return e[j]
        sort_data.sort(key=key_func)

        for i in range(0,len(sort_data),1):
            lsz = i
            rsz = len(sort_data)-i-1
            lp1 = 0
            rp1 = 0
            lp2 = 0
            rp2 = 0
            gini1 = 0
            gini2 = 0
            for k in range(0,i,1):
                if sort_data[k][cols]!=0:
                    lp1=lp1+1
                else:
                    lp2=lp2+1
            for k in range(i,len(sort_data)-1,1):
                if sort_data[k][cols]==0:
                    rp1=rp1+1
                else:
                    rp2=rp2+1
            
            if i == 0:
                gini1=(rsz/(len(sort_data)-1))*(rp1/rsz)*(1 - (rp1/rsz))
                # gini2=(rsz/(len(sort_data)-1))*(rp2/rsz)*(1 - (rp2/rsz))
            elif i == len(sort_data)-1:
                gini1=(lsz/(len(sort_data)-1))*(lp1/lsz)*(1 - (lp1/lsz)) 
                # gini2=(lsz/(len(sort_data)-1))*(lp2/lsz)*(1 - (lp2/lsz))
            else:
                gini1=(lsz/(len(sort_data)-1))*(lp1/lsz)*(1 - (lp1/lsz)) + (rsz/(len(sort_data)-1))*(rp1/rsz)*(1 - (rp1/rsz))
                # gini2=(lsz/(len(sort_data)-1))*(lp2/lsz)*(1 - (lp2/lsz)) + (rsz/(len(sort_data)-1))*(rp2/rsz)*(1 - (rp2/rsz))

            if i!=0:
                thresh_temp = (sort_data[i][j]+sort_data[i-1][j])/2
            else:
                thresh_temp = sort_data[i][j]-0.5

                        
            thresh.append(thresh_temp)
            # gini_temp = min(gini1,gini2)
            gini_val.append(gini1)
            
            if gini1 < gini:
                thr = thresh_temp
                gini = gini1
                if (lp1+rp1)<=(lp2+rp2):
                    categ = 1
                else:
                    categ = 2
        
        if gini<low:
            low=gini
            column=j
        col_gin.append(gini)
        col_thresh.append(thr)
        categ_list.append(categ)
        threshbig.append(thresh)
        ginvals.append(gini_val)
    for i in range(0,rows,1):
        if train_labels.get(i)==None:
            if data[i][column]< col_thresh[column]:
                if categ_list[column]==1:
                    vote_zero[i] += 1
                else:
                    vote_one[i] += 1
            else:
                if categ_list[column]==1:
                    vote_one[i] += 1

                else:
                    vote_zero[i] += 1

#print("#########Predictions############")
for i in range(0,rows,1):
    if train_labels.get(i)==None:
        if vote_zero.get(i)>=vote_one.get(i):
            print(0,"",i)
        else:
            print(1,"",i)
