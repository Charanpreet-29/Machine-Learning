import sys

datafile = sys.argv[1]
f = open(datafile)

data = []
l = f.readline()

##############################
## READ DATA
##############################

while(l != ''):
	a = l.split()
	alen = len(a)
	l2 = []
	for j in range(0, alen, 1):
		l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()


##############################
## READ LABELS
##############################

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
class_size = []
class_size.append(0)
class_size.append(0)
l = f.readline()

while(l != ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	class_size[int(a[0])] = class_size[int(a[0])] + 1
	l = f.readline()
f.close()


ginis_list = []
split = 0
templ = [0, 0]
for j in range(0, cols, 1):
    ginis_list.append(templ)
temp = 0
column = 0

for j in range(0, cols, 1):

    listcolumn = [item[j] for item in data]
    keys = sorted(range(len(listcolumn)), key=lambda k: listcolumn[k])
    listcolumn.sort()
    print("sorted column list",listcolumn)
    print("keys ",keys)
    gini_val = []
    previous_gini = 0
    previous_row = 0
    for k in range(1, rows, 1):

        lsize = k
        rsize = rows - k
        lp = 0
        rp = 0

        for l in range(0, k, 1):
            if (trainlabels.get(keys[l]) == 0):
                lp += 1
        for r in range(k, rows, 1):
            if (trainlabels.get(keys[r]) == 0):
                rp += 1
        gini = (lsize / rows) * (lp / lsize) * (1 - lp / lsize) + (rsize / rows) * (rp / rsize) * (1 - rp / rsize)
        gini_val.append(gini)

        previous_gini = min(gini_val)
        if (gini_val[k - 1] == float(previous_gini)):
            ginis_list[j][0] = gini_val[k - 1]
            ginis_list[j][1] = k
    if (j == 0):
        temp = ginis_list[j][0]
    if (ginis_list[j][0] <= temp):
        temp = ginis_list[j][0]
        column = j
        split = ginis_list[j][1]
        if (split != 0):
            split = (listcolumn[split] + listcolumn[split - 1]) / 2
print("gini:", temp, "column:", column, "split:", split)
