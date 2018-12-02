import numpy as np
import pandas as pd
import os
import csv


CORval=[]
allCOR=[]

dataset = pd.read_csv('data/150407.csv')

Gscore = np.array(dataset[['growthScore']])
FRscore = np.array(dataset[['financialReturnsScore']])
Mscore = np.array(dataset[['multipleScore']])
Iscore = np.array(dataset[['integratedScore']])



Growth = []
for i in range(len(Gscore)):
	Growth.append(Gscore[i][0])
print(Gscore)
print("------")
print(Growth)

FinancialRet = []
for i in range(len(FRscore)):
	FinancialRet.append(FRscore[i][0])


Multiple= []
for i in range(len(Mscore)):
	Multiple.append(Mscore[i][0])

IntFactor = []
for i in range(len(Iscore)):
	IntFactor.append(Iscore[i][0])

y = np.array(dataset['close'])


#CORval.append(files[:-4])
CORval.append(np.corrcoef(Growth, y)[0][1])
CORval.append(np.corrcoef(FinancialRet, y)[0][1])
CORval.append(np.corrcoef(Multiple, y)[0][1])
CORval.append(np.corrcoef(IntFactor, y)[0][1])
allCOR.append(CORval)
CORval=[]

#print (allCOR)