import numpy as np
import pandas as pd
import os

rootdir = '/Users/mhn/Desktop/marquee/data'

i=0 
for files in os.listdir(rootdir):
#print(os.listdir(rootdir))
	if filename.endswith(".cv"):
		dataset = pd.read_csv(files)
		#print(dataset.shape)
		i =+ 1
		print(i)



'''
	Gscore = np.array(dataset[['growthScore']])
	FRscore = np.array(dataset[['financialReturnsScore']])
	Mscore = np.array(dataset[['multipleScore']])
	Iscore = np.array(dataset[['integratedScore']])



	Growth = []
	for i in range(len(Gscore)):
		Growth.append(Gscore[i][0])


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



	CORG=np.corrcoef(Growth, y)[0][1]
	CORFR=np.corrcoef(FinancialRet, y)[0][1]
	CORM=np.corrcoef(Multiple, y)[0][1]
	CORI=np.corrcoef(IntFactor, y)[0][1]

	print(CORG)
	print(CORFR)
	print(CORM)
	print(CORI)
'''