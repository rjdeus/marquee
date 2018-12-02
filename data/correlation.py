import numpy as np
import pandas as pd
import os
import csv

rootdir = '/Users/mhn/Desktop/marquee/data'

CORval=[]
allCOR=[]


for files in os.listdir(rootdir):
#print(os.listdir(rootdir))
	if files.endswith(".csv"):
		dataset = pd.read_csv(files)
		print(dataset.shape)


		Gscore = np.array(dataset[['growthScore']])
		FRscore = np.array(dataset[['financialReturnsScore']])
		Mscore = np.array(dataset[['multipleScore']])
		Iscore = np.array(dataset[['integratedScore']])



		Growth = []
		for i in range(len(Iscore)):
			Growth.append(Gscore[i][0])


		FinancialRet = []
		for i in range(len(Iscore)):
			FinancialRet.append(FRscore[i][0])


		Multiple= []
		for i in range(len(Iscore)):
			Multiple.append(Mscore[i][0])

		IntFactor = []
		for i in range(len(Iscore)):
			IntFactor.append(Iscore[i][0])


		y = np.array(dataset['close'])




		CORval.append(files[:-4])
		CORval.append(np.corrcoef(Growth, y)[0][1])
		CORval.append(np.corrcoef(FinancialRet, y)[0][1])
		CORval.append(np.corrcoef(Multiple, y)[0][1])
		CORval.append(np.corrcoef(IntFactor, y)[0][1])
		allCOR.append(CORval)
		CORval=[]

npCOR=np.array(allCOR)
print(npCOR)
df = pd.DataFrame(npCOR, index=list(range(len(npCOR))), columns=['GSID','G','FR','M','IR'])
print(df)
df.to_csv('Corilation.csv', encoding='utf-8', index=False)


'''


		print(CORG)
		print(CORFR)
		print(CORM)
		print(CORI)

'''