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
	l2.append(1)
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

#eta sample data#eta = 0.01
eta = 0.001 #eta climate data
temp = 1
c = 0
error = 0.0

##############Compute Error###########
for i in range(0, rows, 1):
	if (trainlabels.get(i) != None):
		dp = dot_product(w, data[i], cols)
		sigfn = 1/(1 + math.exp(-1 * dp))
		error += (-trainlabels.get(i) *math.log(sigfn))-((1- trainlabels.get(i))*math.log(sigfn*(math.exp(-1*dp))))

prev_e = error
while(abs(temp)>0.001): #for sample data 0.0000001
	dellf = []
	for j in range(0,cols,1):
		dellf.append(0)
	#################Compute Dellf##############
	temp = 0
	for i in range(0, rows, 1):
		if (trainlabels.get(i) != None):
			dp = dot_product(w, data[i], cols)
			sigfn = 1/(1+math.exp(-1*dp))
			for j in range(0,cols,1):
				dellf[j] += ((trainlabels.get(i)-(sigfn))*data[i][j])

	##################Update W##################
	for j in range(0, cols, 1):
		w[j] += eta*dellf[j]

	##############Compute Error New###########
	error = 0
	for i in range(0,rows,1):
		if trainlabels.get(i)!=None:
			dp = dot_product(w, data[i], cols)
			sigfn = 1/(1+math.exp(-1*dp))
			error += (-trainlabels.get(i)*math.log(sigfn))-((1-trainlabels.get(i))*math.log(sigfn*(math.exp(-1*dp))))	

	c += 1
	print ("error is = ",error, c)
	temp = error - prev_e
	prev_e = error


normw=0
for j in range(0,cols-1,1):
	normw=normw+(w[j]**2)
	print(w[j])
print("\n")
normw=normw**(1/2)
print("||w||=",normw,"\n")

d_origin=w[len(w)-1]/normw
print("W0=",w[len(w)-1])

####Prediction 

print("Distance to origin=",abs(d_origin),"\n")

#########################################
####Prediction
#########################################
for i in range(0, rows, 1):
	if (trainlabels.get(i) == None):
		dp = dot_product(w, data[i], cols)
		if(dp>0):
			print("pred is 1",i)
		else:
			print("pred is 0",i)

