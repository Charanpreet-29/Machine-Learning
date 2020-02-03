import sys
import random
from math import inf
from sklearn.svm import LinearSVC
from sklearn import model_selection;
import os

dataFileName = sys.argv[1]
labelFileName = sys.argv[2]
dataFile = open(dataFileName)
trainingFile = open(labelFileName)

try:
    level_k = [int(sys.argv[3])]
except Exception as e:
    level_k = [10, 100, 1000, 10000]


print(level_k)

labelDict = {}  # label dict
dataMatrix = []

for line in dataFile.readlines():
    row = line.split()
    row = [float(r) for r in row]
    dataMatrix.append(row)

for label in trainingFile.readlines():
    _class, _id = label.split()
    # if int(_class) == 0:
    #     _class = -1
    labelDict.update({int(_id): int(_class)})

trainLabels, trainC, ZtrainOrig = {}, 0, []
testLabels, testC = {}, 0
for i, row in enumerate(dataMatrix):
    if labelDict.get(i, None) != None:
        trainLabels.update({trainC:labelDict.get(i)})
        ZtrainOrig.append(row)
        trainC += 1
    else:
        testLabels.update({testC:i})
        testC += 1


def dotProduct(w, row):
    return sum([w[j] * float(col) for j, col in enumerate(row)])


def transpose(a):
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]


for k in level_k:
    Ztrain = []
    Ztest = []
    for i in range(0, k):
        w = [random.uniform(-1, 1) for i in range(len(dataMatrix[0]))]
        smallest = float(inf)
        largest = float(-inf)

        for row in dataMatrix:
            wtx = dotProduct(w, row)
            if wtx < smallest:
                smallest = wtx
            if wtx > largest:
                largest = wtx

        w0 = random.uniform(smallest, largest)

        zTrain = []
        zTest = []
        for i, row in enumerate(dataMatrix):
            wtx = dotProduct(w, row) + w0
            if labelDict.get(i) != None:
                if (1 + wtx)/2 < 0:
                    zTrain.append(0)
                else:
                    zTrain.append(1)
            else:
                if (1 + wtx) / 2 < 0:
                    zTest.append(0)
                else:
                    zTest.append(1)

        Ztrain.append(zTrain)
        Ztest.append(zTest)

    Ztrain = transpose(Ztrain)
    Ztest = transpose(Ztest)

    model = LinearSVC(max_iter=100000)
    scoreNew = model_selection.cross_val_score(model, Ztrain, list(trainLabels.values()), cv=10)
    scoreOrignal = model_selection.cross_val_score(model, ZtrainOrig, list(trainLabels.values()), cv=10)
    #print("Data File: ", os.path.basename(dataFileName), "Training Label File: ", os.path.basename(labelFileName))
    print("Mean training error on new features data for k=", k, "planes cross validated 10 times is: ", 1-sum(scoreNew)/10)
    print("Mean training error on original features cross validated 10 times is: ", 1-sum(scoreOrignal)/10)

    if k == level_k[-1]:
        predict = model.fit(Ztrain, list(trainLabels.values())).predict(Ztest)
        #for i, val in enumerate(predict):
            #print(val, testLabels.get(i))


