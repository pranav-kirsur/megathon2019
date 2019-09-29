import random
import csv

nDataPoints = 50
nFeatures = 12
nOutputs = 1

allData = []

for i in range(nDataPoints):
    
    curr = [random.random() for i in range(nFeatures+nOutputs)]
    allData += [curr]

with open('features-test.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerows(allData)
