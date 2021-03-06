import sys

datafile = sys.argv[1]

f = open(datafile, 'r')
data = []
i = 0
l = f.readline()

#################
### Read Data ###
#################

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])

print("rows=", rows, " cols=", cols)

f.close()

###############################
##### read training labels ####
###############################

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = [0, 0]
l = f.readline()
while (l != ''):
    a = l.split()
    trainlabels[a[1]] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1
# int count = 0;

# print ("DATA#########",data)
# print ("TRAINLABELS########",trainlabels)
# print ("N#########",n)

##############################
###### compute means #########
##############################

m0 = []
for j in range(0, cols, 1):
    m0.append(1)

m1 = []
for j in range(0, cols, 1):
    m1.append(1)
# print("row", rows)
# print("trainlabels",trainlabels)
for i in range(0, rows, 1):
    if (trainlabels.get(str(i)) != None):
        if (trainlabels.get(str(i)) == 0):
            for j in range(0, cols, 1):
                m0[j] = m0[j] + data[i][j]
                #		print(m0[j])
        if (trainlabels.get(str(i)) == 1):
            for j in range(0, cols, 1):
                m1[j] = m1[j] + data[i][j]
for j in range(0, cols, 1):
    m0[j] = m0[j] / n[0]
    m1[j] = m1[j] / n[1]

# print(m0)
# print(m1)

############################################
#### classification of unlabeled point  ####
############################################

for i in range(0, rows, 1):
    if (trainlabels.get(str(i)) == None):
        d0 = 0
        d1 = 0

        for j in range(0, cols, 1):
            d0 = d0 + ((data[i][j] - m0[j])) ** 2
            d1 = d1 + ((data[i][j] - m1[j])) ** 2

        d0 = d0*0.5
        d1 = d1*0.5

        # d0 = d0 * ((1 / (math.sqrt(2*math.pi) * sd0[j])) * math.exp(-(math.pow(data[i][j]-m0[j],2)/(2*math.pow(sd0[j],2)))))
        #			p1 = p1 * ((1 / (math.sqrt(2*math.pi) * sd1[j])) * math.exp(-(math.pow(data[i][j]-m1[j],2)/(2*math.pow(sd1[j],2)))))

        if (d0 < d1):
            print("0 ", i)
        else:
            print("1 ", i)

##############################################