import sys
import random
import math

########################
##dot product function
########################
def dot_product(refw, refx, cols):
    dp=0
    for j in range(0, cols, 1):
        dp += refw[j]*refx[j]
    return dp


datafile = sys.argv[1]
f = open(datafile)

data = []
i = 0
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
        if j == (alen-1) :
            l2.append(float(1))
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
    if int(a[0]) == 0:
        trainlabels[int(a[1])] = -1
    else:
        trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    class_size[int(a[0])] += 1


###############################
###Initialize W
###############################

w = []
for j in range(0, cols, 1):
    w.append(0)
    w[j] = (0.02 * random.uniform(0,1)) - 0.01

#################################
##Gradient Descent Iteration
#################################

eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
bestobj = 1000000000000000000
temp = 1
c = 0
error = 0.0

##############Compute Error###########
for i in range(0, rows, 1):
    if (trainlabels.get(i) != None):
        dp = dot_product(w, data[i], cols)
        test = (trainlabels.get(i)*dp)
        if (test <1):
            error += (trainlabels.get(i)-(1-test))

prev_e = error
while(abs(temp)>0.001):
    dellf = []
    for j in range(0,cols,1):
        dellf.append(0)
    #################Compute Dellf##############
    temp = 0
    for i in range(0, rows, 1):
        if (trainlabels.get(i) != None):
            dp = dot_product(w, data[i], cols)
            for j in range(0,cols,1):
                test=(trainlabels.get(i)*dp)
                if test<1:
                    dellf[j] += (data[i][j]*trainlabels.get(i))
    
    best_eta = 1
    for etas in range(0, len(eta_list), 1):
        eta = eta_list[etas]
    ##################Update W##################
        for j in range(0,cols,1):
            w[j] += eta*dellf[j]

    ##############Compute Error New###########
        error = 0
        lc = 0
        for i in range(0,rows,1):
            if trainlabels.get(i)!=None:
                lc += 1
                dp = dot_product(w, data[i], cols)
                test=(trainlabels.get(i)*dp)
                if test<1:
                    error += (1-test)
        obj = error
        if obj < bestobj:
            bestobj = obj
            best_eta = eta
        for j in range(0,cols,1):
            w[j] -= (eta*dellf[j])

    eta = best_eta

    for j in range(0,cols,1):
        w[j] += (eta*dellf[j])
    error = 0
    lc = 0
    for i in range(0,rows,1):
        if trainlabels.get(i)!=None:
            lc = lc +1
            dp = dot_product(w, data[i], cols)
            test = (trainlabels.get(i)*dp)
            if test < 1:
                error += (1 - test)

    c += 1
#    print ("error is = ",error, c)
    temp = error - prev_e
    prev_e = error


normw=0
for j in range(0,cols-1,1):
    normw=normw+(w[j]**2)
#    print(w[j])
#print("\n")
normw=normw**(1/2)
#print("||w||=",normw,"\n")

d_origin=w[len(w)-1]/normw
#print("W0=",w[len(w)-1])

####Prediction 

#print("Distance to origin=",abs(d_origin),"\n")

#########################################
####Prediction
#########################################
for i in range(0, rows, 1):
    if (trainlabels.get(i) == None):
        dp = dot_product(w, data[i], cols)
        if(dp>0):
            print("1",i)
        else:
            print("0",i)

